from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from flask_bcrypt import Bcrypt
import cryptography 
from cryptography.fernet import Fernet

#csrf
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
class csrfform(FlaskForm):
    country_name = StringField('country_name')   
#end csrf
bcrypt = Bcrypt()
app = Flask(__name__)
app.secret_key = 'your secret key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '5002nevsmai!'
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)
@app.route('/', methods=['GET', 'POST']) 
def login():
    msg = ''
    
    #csrf
    form = csrfform()
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        user_hashpwd = account['password']
        if account and bcrypt.check_password_hash( user_hashpwd, password) :

            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            encrypted_email = account['email'].encode()
            file = open('symmetric.key', 'rb')
            key = file.read()
            file.close()
            f = Fernet(key)
            decrypted_email = f.decrypt(encrypted_email)
            
            return redirect(url_for('profile'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html',msg='', form=form)
 


@app.route('/register', methods=['GET', 'POST'])
def register():
    #csrf
    form = csrfform()
    
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        email = email.encode()
        hashpwd = bcrypt.generate_password_hash(password)
        key = Fernet.generate_key()
        with open("symmetric.key", "wb") as fo:
            fo.write(key)
        f = Fernet(key)
        encrypted_email = f.encrypt(email)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, hashpwd, encrypted_email,))
        mysql.connection.commit()
        msg = 'You have successfully registered!'

    elif request.method == 'POST':
        msg = 'Please fill out the form!'
    return render_template('register.html', msg=msg, form=form)

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        encrypted_email = account['email'].encode()
        file = open('symmetric.key', 'rb')
        key = file.read()
        file.close()
        f = Fernet(key)
        decrypted_email = f.decrypt(encrypted_email)
        print(decrypted_email)
        account['email'] = decrypted_email.decode()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/ip')
def ip():
    if 'loggedin' in session:
        return render_template('test.html', username=session['username'])
    return redirect(url_for('login'))

if __name__ == '__main__': 
    app.run()
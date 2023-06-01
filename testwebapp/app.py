from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')


connect = sqlite3.connect('database.db')
connect.execute(
	'CREATE TABLE IF NOT EXISTS PARTICIPANTS (name TEXT, \
	email TEXT, city TEXT, country TEXT, phone TEXT, phoneadd TEXT)')
connect.execute(
	'CREATE TABLE IF NOT EXISTS device_info (os TEXT, \
	os_version TEXT, browser TEXT, browser_version TEXT)')


@app.route('/join', methods=['GET', 'POST'])
def join():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		city = request.form['city']
		country = request.form['country']
		phone = request.form['phone']
		phoneadd = request.form['phone'] + "phone"

		with sqlite3.connect("database.db") as users:
			cursor = users.cursor()
			cursor.execute("INSERT INTO PARTICIPANTS \
			(name,email,city,country,phone,phoneadd) VALUES (?,?,?,?,?,?)",
						(name, email, city, country, phone, phoneadd))
			users.commit()
		return render_template("index.html")
	else:
		return render_template('join.html')


@app.route('/participants')
def participants():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM PARTICIPANTS')
	data = cursor.fetchall()
	return render_template("participants.html", data=data)
@app.route('/participant')
def participant():
	connect = sqlite3.connect('database.db')
	cursor = connect.cursor()
	cursor.execute('SELECT * FROM device_info')
	data = cursor.fetchall()
	return render_template("participant.html", data=data)

@app.route("/api/device-info", methods=["POST"])
def device_info():

  device_info = request.get_json()

  if not device_info:
    return jsonify({"status": 400, "message": "Invalid device information"})
  db = sqlite3.connect("database.db")
  cursor = db.cursor()
  cursor.execute("INSERT INTO device_info (os, os_version, browser, browser_version) VALUES (?, ?, ?, ?)", (device_info["os"], device_info["os_version"], device_info["browser"], device_info["browser_version"]))
  db.commit()
  db.close()
  return jsonify({"status": 200, "message": "Device information stored successfully"})

if __name__ == "__main__":
    app.run()

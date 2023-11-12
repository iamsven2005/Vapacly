import os
import pathlib

import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests

from flask import Flask, render_template, request, redirect, url_for, session, abort
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
from datetime import datetime
class csrfform(FlaskForm):
    country_name = StringField('country_name')   
app = Flask(__name__)
app.secret_key = 'your secret key'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "2"

GOOGLE_CLIENT_ID = "981934456193-1oa6nc28h5g4fqme71poim0mmisa65ih.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret_981934456193-1oa6nc28h5g4fqme71poim0mmisa65ih.apps.googleusercontent.com.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost/callback"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wrapper

@app.route("/login")
def login():
    
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return redirect(authorization_url)

@app.route('/callback', methods=['GET', 'POST'])
def callback():
    flow.fetch_token(authorization_response=request.url)


    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )


    session["google_id"] = id_info.get("sub")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    session["pp"]= id_info
    return redirect("/protected_area")

@app.route("/protected_area")
@login_is_required
def protected_area():
    return f" {session['pp']} Hello {session['name']} this is your email <h1>{session['email']}</h1><br>password<h1></h1>! <br/> <a href='/logout'><button>Logout</button></a>"
if __name__ == '__main__': 
    app.run(port="80", debug=True)

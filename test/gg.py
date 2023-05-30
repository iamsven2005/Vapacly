import flask
from flask import *
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(date)
    return render_template("index.html", date=date)
    
if __name__ == "__main__":
    app.run()

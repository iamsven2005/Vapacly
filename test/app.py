#https://www.geeksforgeeks.org/pass-javascript-variables-to-python-in-flask/

from flask import Flask,render_template, request

app = Flask(__name__,template_folder="templates")

@app.route("/")
def hello():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	data = request.form.get('data')
	return data

if __name__ == '__main__':
	app.run(debug=True)



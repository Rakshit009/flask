from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
	return '<h1>This is Rakshit karande </h1>'

@app.route('/info')
def info():
	return '<h1>This is Sanchani Karande</h1>'

@app.route('/friend/<name>')
def friend(name):
	return '<h1>My friends name is {}</h1>'.format(name)


if __name__ == '__main__':

	app.run(debug=True)
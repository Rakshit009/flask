from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('friend.html')

@app.route('/base')
def base():
	return render_template('base.html')

@app.route('/friends/<name>')
def friends(name):
	return render_template('friends.html', name=name)

if __name__ == "__main__":

	app.run(debug=True)
	

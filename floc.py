from flask import Flask,render_template 

app = Flask(__name__)

@app.route('/')
def flowControl():
	list1 = ['Rakshit','Akash','Nayum','Dipesh','Prasad']
	return render_template('floc.html',list1=list1)

if __name__ == '__main__':

	app.run(debug=True)
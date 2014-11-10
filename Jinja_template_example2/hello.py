from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/' , methods = ['GET', 'POST'])
def index():
	name = None
	#request.method -->used to differentiate between GET and POST reqs
	if request.method == 'POST' and 'name' in request.form:
		name = request.form['name']
	return render_template('index.html' , name = name)

if __name__ == '__main__':
	app.run(debug = True)

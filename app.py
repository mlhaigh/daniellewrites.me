from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
app.config['DEBUG'] = True # disable for deployment

@app.route('/')
def hello():
	print "test"
	return render_template('hello.html')

@app.route('/search', methods=["GET", "POST"])
def search():
	if request.method == "POST":
		url = "http://writingexercises.co.uk/php/firstline.php" 
		print request.form
		response = requests.get(url)
		response_dict = response.text
		return render_template("results.html", api_data=response_dict)
	else:
		return render_template("search.html")

@app.errorhandler(404)
def not_found(error):
	return "Something went wrong, Danielle.  I'm Sorry.", 404

@app.errorhandler(500)
def internal_server_error(error):
	return "Something went wrong, Danielle.  I'm Sorry.", 500

if __name__ == '__main__':
	app.run(host='0.0.0.0')

	

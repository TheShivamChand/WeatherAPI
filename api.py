from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route('/temperature',methods=['POST'])
def temperature():
	zipcode=request.form['zip']
	r=requests.get("https://api.openweathermap.org/data/2.5/weather?zip="+zipcode+",in&appid=bebfbb7391cb5af0833aebddd96f4e18")
	json_obj=r.json()
	temp_k=float(json_obj['main']['temp'])
	temp_c= round(temp_k-273.15,2)
	cityx=json_obj['name']
	return render_template('temp.html',city=cityx,temp=temp_c)

@app.route('/index')
def index():
	return render_template("index.html")

if __name__== '__main__':
	app.run(debug=True)
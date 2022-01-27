import re
from flask import Flask, render_template
import datetime
from  datetime import date



app = Flask(__name__)

@app.route('/')
def home():
    	return render_template('/home.html')

@app.route('/about/')
def about():
    	return render_template('/about.html')


def get_date_for_meeting():
	dt = date.today()
	fmt = datetime.datetime.strptime(str(dt), "%Y-%m-%d").strftime("%A")
	print(fmt)
	if fmt == "Tuesday":
		return f"{fmt}: After School"
 	
	elif fmt == "Thursday":
		return f"{fmt}: After School"
				
	elif fmt == "Saturday":
		return f"{fmt}: 10 AM in the morning"
	else:
		return f"{fmt}: N/A"
    			
    			



@app.route("/meetings/")
def meetings():
 upcoming = get_date_for_meeting()
 return render_template("/meetings.html", meet=upcoming)
#"https://salesianhigh.org/wp-content/uploads/2020/02/cross_images.png"

@app.route("/announcements/")
def announcements():
    	return render_template("/announcements.html")

if __name__ == "__main__":
	app.run(debug=True)

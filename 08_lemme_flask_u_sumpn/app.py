#Maryann Foley
#SoftDev1 pd8
#K08 -- Fill yer flask
#2018-09-19    

from flask import Flask,url_for
app=Flask(__name__)


@app.route("/")
def home():
	retStr="<h3>Welcome!</h3>"
	retStr+="<h3><a href='"+url_for("intro")+"'>Introduction</a>"
	return retStr

@app.route("/introduction")
def intro():
	retStr="<h3><a href='"+url_for("home")+"'>Home</a>"
	retStr+="<p>Hello my name is Maryann.</p>"
	retStr+="<a href='"+url_for("pod")+"'>Click here for some things I like</a>"
	return retStr

@app.route("/podcasts")
def pod():
	retStr="<h3><a href='"+url_for("home")+"'>Home</a><br>"
	retStr+="<h4>My favorite podcasts</h4>"
	retStr+='<table border="1"><tr><th>Category</th><th>Thing!</th></tr><tr><td>Comedy podcast</td><td>My brother, my brother, and me</td></tr>'
	retStr+="<tr><td>DnD Podcast</td><td>The Adventure Zone</td></tr><tr><td>Non-fiction podcast</td><td>99% Invisible</td></tr>"
	return retStr

if __name__=="__main__":
	app.run(debug=True)
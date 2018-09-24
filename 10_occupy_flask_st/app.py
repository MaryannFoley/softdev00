#Maryann Foley
#SoftDev1 pd8
#K10 -- Jinja tuning
#2018-09-19    

from flask import Flask,url_for,redirect,render_template
from occupation import main
app=Flask(__name__)


@app.route("/")
@app.route("/occupations")
def occupation():
	occ,jobs=main()
	return render_template("template.html", occupation=occ,jobs=jobs)

if __name__=="__main__":
	app.run(debug=True)
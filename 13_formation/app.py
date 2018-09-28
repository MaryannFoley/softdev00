from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def something():
	print(app)
	print(request)
	print(request.method)
	if request.method == "GET" and request.args and request.args["Username"] and request.args["Username"] is not "":
		print(request.args)
		return render_template("loggedIn.html",uname=request.args["Username"],method="get")
	elif request.method == "POST" and request.form:
		print(request.form)
		return render_template("loggedIn.html",uname=request.form["Username"],method="post")
	else:
		return render_template("login.html")

if __name__ == "__main__":
    app.debug = True
    app.run()

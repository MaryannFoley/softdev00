
from flask import Flask, render_template, session,url_for,redirect
import os
import csv
app = Flask(__name__)

@app.route("/", methods=['POST'])
def auth():
    return render_template("login.html",Title = 'Login')

@app.route("/", methods=['POST'])
def auth():
    return render_template("login.html",Title = 'Login')

if __name__ == "__main__":
    app.debug = True
    app.run()

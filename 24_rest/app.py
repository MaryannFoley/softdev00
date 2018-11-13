from flask import Flask, render_template
import urllib.request
app = Flask(__name__)


@app.route("/")
def something():
    request=urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=4Gt3nL0hLF4rNbj9aifudBMdz0alxDewjaOIN2Rx")
    raw=request.read()
    json=raw.loads()
    print(json)
    return "<h3>Homework template</h3>"
    #render_template is also useful

if __name__ == "__main__":
    app.debug = True
    app.run()

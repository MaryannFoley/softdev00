from flask import Flask, render_template
import urllib.request
import json
app = Flask(__name__)


@app.route("/")
def something():
    request=urllib.request.urlopen("https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=4Gt3nL0hLF4rNbj9aifudBMdz0alxDewjaOIN2Rx")
    raw=request.read()
    print(raw)
    jdict=json.loads(raw)
    print(jdict)
    url = jdict["url"]
    print(url)
    planet=jdict["resource"]["planet"].upper()
    date=jdict["date"]
    date=date.split("T")


    return render_template("index.html",img=url, planet=planet,date=date)
    #render_template is also useful

if __name__ == "__main__":
    app.debug = True
    app.run()

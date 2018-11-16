#Maryann Foley
#SoftDev1 pd8
#K25 -- Getting More REST
#2018-11-15

import urllib.request
import json

from flask import Flask, render_template

app = Flask(__name__)

URL_STUB1="https://ghibliapi.herokuapp.com/films/12cfb892-aac0-4c5b-94af-521852e46d6a"
URL1=URL_STUB1
URL_STUB2="https://collectionapi.metmuseum.org/public/collection/v1/objects/435885"
URL2=URL_STUB2
URL_STUB3="https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=json&callback=callback&q_track=Maud%20Gone&q_artist=Car%20Seat%20Headrest&apikey="
KEY="3a8e7a04c7f287c1f7293f7d07158e29"
URL3=URL_STUB3+KEY

@app.route("/")
def something():
    request1=urllib.request.urlopen(URL1)
    raw1=request1.read()
    jdict1=json.loads(raw1)
    #===================================
    request2=urllib.request.urlopen(URL2)
    raw2=request2.read()
    jdict2=json.loads(raw2)
    #===================================
    request3=urllib.request.urlopen(URL3)
    raw3=request3.read()
    jdict3=json.loads(raw3)
    lyrics=jdict3["message"]["body"]["lyrics"]["lyrics_body"]
    print(lyrics)
    lyrics=lyrics.split("\n")
    return render_template("index.html",one=jdict1,two=jdict2,lyrics=lyrics)

if __name__ == "__main__":
    app.debug = True
    app.run()

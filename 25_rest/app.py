#Maryann Foley
#SoftDev1 pd8
#K25 -- Getting More REST
#2018-11-15

import urllib.request
import json

from flask import Flask, render_template

app = Flask(__name__)

URL_STUB="https://transit.api.here.com/v3/route.json?routing=all&dep=40.6146455,-74.0369021&arr=40.7173116,-74.0144598&time=2018-11-15T07%3A30%3A00&"
KEY="app_id=Yzt1XILAn7f4v6WSPBW3&app_code=yAvSoCdhn5jMmQk-CFlnqA"
URL=URL_STUB+KEY

@app.route("/")
def something():
    request=urllib.request.urlopen(URL)
    raw=request.read()
    #print("Raw JSON")
    #print("===========")
    #print(raw)
    #print("===========")
    jdict=json.loads(raw)
    #print("Dictonary")
    #print("===========")
    #print(jdict)
    #print("===========")
    trips=[]
    for key in jdict["Res"]["Connections"]["Connection"]:
        trip=[]
        for step in key["Sections"]["Sec"]:
            #print("===============")
            #print(step)
            #print("===============")
            stepp=[]
            if "Addr" in step["Dep"]:
                stepp.append("START")
            elif "Stn" in step["Dep"]:
                stepp.append(step["Dep"]["Stn"]["name"])
            if step["Dep"]["Transport"]["mode"] == 20:
                stepp.append(["Walk",step["Journey"]["distance"]])
            else:
                stepp.append(["Take",step["Dep"]["Transport"]["name"]])
            if "Addr" in step["Arr"]:
                stepp.append("END")
            elif "Stn" in step["Arr"]:
                stepp.append(step["Arr"]["Stn"]["name"])
            #print(stepp)
            trip.append(stepp)
        trips.append(trip)
    print("TRIPS")
    print("========")
    print(trips)
    print("========")
    return render_template("index.html",trips=trips)

if __name__ == "__main__":
    app.debug = True
    app.run()

#Quacking Geese: Maryann Foley and Robin Han
#SoftDev1 pd8
#K16:No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O



DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = ""
with open("peeps.csv", newline = '\n') as csvfile:
    reader=csv.DictReader(csvfile)
    command+="CREATE TABLE peeps (name TEXT, id INTEGER, age INTEGER);"
    for row in reader:
            command+="INSERT INTO peeps VALUES ('"+row['name']+"', "+row['id']+", "+row['age']+");"
            
#####c.execute(command)    #run SQL statement only executes one at a time
 ##create second table

with open("courses.csv", newline = '\n') as csvfile2:
    reader=csv.DictReader(csvfile2)
    command+="CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER);"
    for row in reader:
            command+="INSERT INTO courses VALUES ('"+row['code']+"', "+row['id']+", "+row['mark']+");"

c.executescript(command)    #run SQL statement2
#==========================================================

db.commit() #save changes
db.close() #close database
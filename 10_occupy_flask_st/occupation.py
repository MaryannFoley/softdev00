#Updated to return both the dict and the occ and removed test cases 

import random

def main():
    file = open("./data/occupations.csv", "r")
    #open the data file and reads the contents

    flines = file.readlines()[1:]
    #readlines reads the individual lines of the file starting from the second

    dict = {}
    #initializes the dictionary

    for line in flines:
        #print(line)
        quote = False
        #initializes whether or not the occupation is in quotes as false
        occupation = ""
        #initializes the occupation name
        num = False
        #initializes whether we are parsing through the percent as false
        percent = ""
        #initializes the percent string
        link = False
        #initializes whether we are parsing through the link as false
        url = ""
        #initializes the url string
        for character in line:
            if character == "\"":
                quote = not quote
                #if a char is a quote, either turn quote true to start the quote
                #or turn it false if the quote just ended.
            elif character == ",":
                if quote:
                    occupation += character
                    #if the comma in inside a quote, add it as part of the
                    #occupation name.
                else:
                    if num:
                        num=False
                        link=True
                    else:
                        num = True
                        #if comma is not inside quote, start recording the percent
            else:
                if num:
                    percent += character
                    #if char is not a quote or a comma, and we are
                    #recording the percent, add the char to the percent string
                elif link:
                    url+=character
                else:
                    occupation += character
                    #if char is not quote, comma, or part of the percent number,
                    #add char to the occupation string.
        #print(occupation)
        #print(percent)
        url = url.replace("\n", "")
        #newlines were added to the end of the percent string from the end
        #of every line, so we must remove them.
        dict[occupation]= [(float)(percent),url]
        #the occupation and percent of each line are logged in the dictionary
    randNum=random.random()*dict["Total"][0]
    #gets a random number with one decimal from 0 to 99.7, starts at .1 because starting at 0 would mean that if the first occ had 0%, it could be chosen
    counter=0.0
    for occ in dict:
        if occ=="Total":
            print("current counter: ",counter)
            continue
            # in case total comes out of order because it would always become true
        if randNum <= counter+dict[occ][0]: #check if the rand number is between the original counter # and the max percent for the occ
            return (occ,dict)
        else:
            counter+=dict[occ][0]
    return ("Error",dict)

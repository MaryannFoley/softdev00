# K #06: StI/O: Divine your Destiny!

In the notes&code repo is a .csv file containing information about occupations in the United States (courtesy of Mr. Brooks). Here is a snippet of two lines of the file:

    Legal,0.8

    "Education, training and library",6.1

The first item is the name of the occupation and the second is the percentage of the U.S. workforce it comprises. Note the quotation marks surrounding an occupation containing commas.

Your job (as a DUO):

Write a Python script to read in the file and build an appropriate dictionary from it. Make sure the percentages are stored as numbers.

Create a function that returns a randomly selected occupation where the results are weighted by the percentage given. For example, there should be a 6.1% chance that "Education, training and library" is returned.


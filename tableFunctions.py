# Turn CSV file into an HTML table
# Written by J Folding

import numpy as np
import csv
from tabulate import tabulate   #external library to convert list into html table
# import simpletable
import codecs

tableData = []

#Read CSV file and turn save into an array called data

with open(r'C:\Users\jfolding\PycharmProjects\untitled\data\EspritPCB.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        # print(row)
        tableData.append(row)


#remove the heading so that it won't show up in the table
tableData.pop(0);
#save it to html file
h = open("EspritPCB.html", "w")
htmlText = (tabulate(tableData, tablefmt='html'))
# f.write("Now the file has more content!")
h.write(htmlText)

# print(htmlText)


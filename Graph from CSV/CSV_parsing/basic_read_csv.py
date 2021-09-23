import csv
import os


def rinseBimCSV():

    inputFileName = "\Graph from CSV\BIM_Original.csv"
    outputFileName = "cleanBIM.csv"
    filename = os.path.dirname(os.getcwd())+inputFileName
    print(filename)

    # open input CSV file as source
    # open output CSV file as result
    with open(filename, "r") as source:
        reader = csv.reader(source)
        
        with open(outputFileName, "w") as result:
            writer = csv.writer(result)
            for r in reader:
                
                # Use CSV Index to remove a column from CSV
                #r[3] = r['year']
                writer.writerow((r[0], r[2], r[3], r[4], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14]))
    print(outputFileName + "saved successfully")


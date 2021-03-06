import csv
import os
import errno
from pathlib import Path

def rinseBimCSV():

    serialNumber = "EDM129 URA007"
    # inputFileName = "\Graph from CSV\BIM_Original.csv"
    inputFileName = "\BIM.csv"  #when running via main.py file use this line
    # outputFileName = f"\{serialNumber}cleanBIM.csv"
    outputFileName = "\cleanBIM.csv"
    savePath = str(Path(__file__).absolute().parent)
    fullSavePath = savePath  + "\BIM Logs"
    # inputFile = os.path.dirname(os.getcwd())+inputFileName
    inputFile = os.getcwd()+inputFileName           #use when running from main file
    outputFile = fullSavePath + outputFileName
    # print(fullSavePath)
    ##Create directory to store file in
    if not os.path.exists(os.path.dirname(outputFile)):
        try:
            os.makedirs(os.path.dirname(outputFile))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

   
    # print(inputFile)
    # print(outputFile)

    # open input CSV file as source
    # open output CSV file as result
    with open(inputFile, "r") as source:
        reader = csv.reader(source)
        
        with open(outputFile, "w") as result:
            writer = csv.writer(result)
            for r in reader:
                
                # Use CSV Index to remove a column from CSV
                #r[3] = r['year']
                writer.writerow((r[0], r[2], r[3], r[4], r[6], r[7], r[8], r[9], r[10], r[11], r[12], r[13], r[14]))
        print(outputFile + " saved successfully")


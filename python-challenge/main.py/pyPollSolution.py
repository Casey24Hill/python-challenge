# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:09:23 2018

@author: casey
"""

#import os and CSV to read file
import os
import csv

os.chdir(r"C:\Users\casey\python-challenge\PyPoll")

list = os.listdir("./raw_data")
number_files = len(list)

# Grab Election CSV file

for numbers in range(number_files):
    electioncsv = os.path.join('raw_data',"election_data.csv")
    
# Set empty list variables
    County= []
    Candidate = []
    CandidateUnique =[]
    CVoteCount = []
    CVotePercent =[]
    TotalCount = 0

# Open raw data file 
    with open(electioncsv,'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
            #skip headers
        next(csvReader, None)

        for row in csvReader: 
            TotalCount = TotalCount + 1
            Candidate.append(row[2])
        for x in set(Candidate):
            CandidateUnique.append(x)
            cc = Candidate.count(x)
            CVoteCount.append(cc)
            CVotePercent.append(Candidate.count(x)/TotalCount)
        
        Winner = CandidateUnique[CVoteCount.index(max(CVoteCount))]

    
    with open('Election_Results.txt', 'w') as text:
        text.write("Election Results"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Vote: " + str(TotalCount) + "\n")
        text.write("----------------------------------------------------------\n")
        for i in range(len(set(Candidate))):
            text.write(CandidateUnique[i] + ": " + str(round(CVotePercent[i]*100,1)) +"% (" + str(CVoteCount[i]) + ")\n")
        text.write("----------------------------------------------------------\n")
        text.write("Winner: " + Winner +"\n")
        text.write("----------------------------------------------------------\n")
## Milton Li, 2017
## Converts the text output file from the spectrophotometer into a csv file for processing with ReferenceError

import sys
import csv

## First argument: input .txt file
## Second argument: temporary .txt holding file
## Third argument: output .csv file
input = sys.argv[1]
processed = sys.argv[2]
output = sys.argv[3]

f = open(input, "r")
p = open(processed, "w")
o = open(output, "w+")

recur = False

for line in f.readlines():
    if "Peaks" in line:
        recur = False
        break
    
    elif recur:
        if line != "\n":
            p.write(line)
            print(line)
    
    elif "Data" in line:
        recur = True
p.close()
p = open(processed, "r")

## Reads into the csv reader with a TAB delimiter
in_txt = csv.reader(p, delimiter='\t')
out_csv = csv.writer(o)
out_csv.writerows(in_txt)
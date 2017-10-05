#!/usr/bin/python
import csv
import sys
import os.path

# validate command line
if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " inputfile outputfile"
    sys.exit()
inputfile, outputfile = sys.argv[1:]
if not os.path.isfile(inputfile):
    print "input file " + inputfile + " doesn't exit"
    sys.exit()
if os.path.isfile(outputfile):
    print "output file " + outputfile + " already exists, overwrite?"
    answer = raw_input("Enter 'Y' to overwrite, anything else to exit: ")
    if answer[0] != 'Y':
        sys.exit()

f = open(inputfile)
of = open(outputfile,"w")
csv_f = csv.reader(f)
seen_header = 0
for row in csv_f:
    if not seen_header:
        seen_header = 1
        continue
    of.write(row[0].capitalize() + "\n")

of.close()
f.close()

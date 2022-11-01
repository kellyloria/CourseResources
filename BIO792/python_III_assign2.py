#!/usr/bin/env python3

# script for part 2 of python III assignment
# Goal: open flies.txt file (3 columns, [ID, day/night, flight time], tab delim.)
# add flight times to a list ONLY if they occurred at night
# write list to outfile

import sys

InFile = sys.argv[1]
IN = open(InFile, 'r')
OUT = open("flies_out.txt", "w")

LineNumber = 0
FlightLengths = []
for Line in IN:
    Line = Line.strip('\n')
    if Line.split('\t')[1] == "N":
       FlightLengths.append(Line.split('\t')[2])
    LineNumber += 1

OUT.write(','.join(FlightLengths))
# ^ output formatted as comma separated values

IN.close()
OUT.close()
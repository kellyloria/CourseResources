#!/usr/bin/env python3

# nice easy script for part 1 of python III assignment
# Goal: open genenames.txt file, extract names of genes with for loop (column 2, tab delim.)
# add those gene names to a list and print list for confirmation

import sys

InFile = sys.argv[1]
IN = open(InFile, 'r')

LineNumber = 0
GeneNames = []
for Line in IN:
    Line = Line.strip('\n')
    GeneNames.append(Line.split('\t')[1])
    LineNumber += 1

print(GeneNames)

IN.close()
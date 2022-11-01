#!/usr/bin/env python3

import sys
import re

# [1:] allows any number of input files to be specified and will calculate totals for each
InFile = sys.argv[1:]

# function to reset count variables after processing of each file
def reset():
    global Eco, Mse, Hind, SeqCnt
    [Eco, Mse, Hind, SeqCnt] = [0, 0, 0, 0]
reset()

# some helpful variables to keep loops clean
[EcoSeq, MseSeq, HindSeq] = ["GAATTC", "TTAA", "AAGCTT"]
FileCnt = 0

for IN in InFile: # in each file passed too sys.argv...
    IN = open(InFile[FileCnt], 'r') # process each line
    for Seq in IN:
        Seq = Seq.strip('\n')
        if re.search("^>", Seq): # count ID lines towards sequence total, but don't do anything with this information
            SeqCnt += 1
        else: # count each occurrence of enzyme sites within sequence and add to total for file
            Eco += len(re.findall(EcoSeq, Seq))
            Mse += len(re.findall(MseSeq, Seq))
            Hind += len(re.findall(HindSeq, Seq))
    print("In file %s there are:\n  %i total sequences\n  %i EcoRI cut sites\n  %i Mse1 cut sites\n  %i HindIII cut sites" %(InFile[FileCnt], SeqCnt, Eco, Mse, Hind)) # print summary once each file has processed
    FileCnt +=1 # allow for next file in InFile to be processed
    reset() # reset count variables for new file
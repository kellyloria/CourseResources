#!/usr/bin/env python3

import sys
import re

# [1:] allows any number of input files to be specified and will calculate totals for each
InFile = sys.argv[1:]

# function to reset count variables after processing of each file
def reset():
    global ATcnt, ATCcnt, GAcnt, SeqCnt
    [ATcnt, ATCcnt, GAcnt, SeqCnt] = [0, 0, 0, 0]
reset()

# some helpful variables to keep loops clean
FileCnt = 0

for IN in InFile: # in each file passed to sys.argv...
    IN = open(InFile[FileCnt], 'r') # process each line
    FileName = InFile[FileCnt].split('_')[0]
    OUTat = open((FileName + "_AT_ssr_sequences.txt"), "w")
    OUTatc = open((FileName + "_ATC_ssr_sequences.txt"), "w")
    OUTga = open((FileName + "_GA_ssr_sequences.txt"), "w")
    for Line in IN:
        Line = Line.strip('\n')
        Fasta = Line
        Seq = IN.readline()
        Seq = Seq.strip('\n')
        if len(re.findall("(AT){4,}", Seq)) > 0:
            Indiv = Fasta + "," + Seq + "," + "\n" # could easily modify this format towards fasta, tab delimited, no line breaks, etc.
            OUTat.write(Indiv)
            ATcnt += 1
        elif len(re.findall("(ATC){4,}", Seq)) > 0:
            Indiv = Fasta + "," + Seq + "," + "\n"
            OUTatc.write(Indiv)
            ATCcnt += 1
        elif len(re.findall("(GA){4,}", Seq)) > 0:
            Indiv = Fasta + "," + Seq + "," + "\n"
            OUTga.write(Indiv)
            GAcnt += 1
        SeqCnt += 1
    print("In file %s there are:\n  %i total sequences\n  %i AT SSRs\n  %i ATC SSRs\n  %i GA SSRs" %(InFile[FileCnt], SeqCnt, ATcnt, ATCcnt, GAcnt)) # print summary once each file has processed
    FileCnt +=1 # allow for next file in InFile to be processed
    reset() # reset count variables for new file
    OUTat.close()
    OUTatc.close()
    OUTga.close()


#!/usr/bin/env python3

# script for part 3 of python III assignment
# Goal: open no60_intron_IME file (fastq)
# write to output a file with sequence ID, sequence length, GC proportion of sequence
# have a summary statement printed detailing total number of sequences and average GC content

import sys
import re

InFile = sys.argv[1]
IN = open(InFile, 'r')
OUT = open("no60_intron_IME_out.txt", "w")

TotalSeq = 0
TotalBases = 0
TotalGCs = 0
GCPropTotal = 0
# ^ three variables above would be used to calculate global GC proportion if all bases from all samples were pooled
# or per sequence average where each sequence is weighted equally (likely more desireable)
SeqInfo = []

def GC_cnt(seq):
    return seq.count("G") + seq.count("C")

for Seq in IN:
    Seq = Seq.strip('\n')
    if re.search("^>", Seq):
        SeqInfo.append(Seq)
    else:
        SeqInfo.append(len(Seq))
        SeqInfo.append(format((GC_cnt(Seq) / len(Seq)), ".3f")) # added some formatting here just to make it cleaner when coerced to a string
        TotalSeq += 1
        TotalBases += len(Seq)
        TotalGCs += GC_cnt(Seq)
        GCPropTotal += (GC_cnt(Seq) / len(Seq))


# average GC calculations based on incremented variables
AvgPerSeq = GCPropTotal / TotalSeq
AvgPooled = TotalGCs / TotalBases

# Can play with output formatting settings here...
# .join() requires coersion of ints/floats to strings (done here with map())
# '\t' separator would be ideal if trying to understand output structure with more/less 
# but the alignment isn't perfect because of different ID name lengths
OutputStr = ','.join(map(str, SeqInfo))
FormOutStr = OutputStr.replace(">", "\n>")

OUT.write(FormOutStr)

IN.close()
OUT.close()

# summary print statement
print("Total sequences: %i\nAvg. GC content per sequence: %.3f\nAvg. GC content across pooled sequences: %.3f" %(TotalSeq, AvgPerSeq, AvgPooled))
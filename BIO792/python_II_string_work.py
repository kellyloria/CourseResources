#!/usr/bin/env python3

import re
# Not sure why the assignment wants to use str.replace() when re.sub() makes a lot more sense...

DNA_Info = "SAMPLE_110 Pop3 atatctcgcggggtttatatatattatttaaa"
DNA_seq = re.sub('[^atcg]','', DNA_Info).upper()
# ^ replaces any characters NOT a, t, c, or g with nothing (effectively deleting) then converts that string to uppercase values
# works in this case b/c sample ID is all capitalized (i.e. capital A/T/C/Gs get deleted)
# would have to consider other treatment if sequences was tagged differently (e.g. str.split with ' ' character, or some regex that considers character on each side of an a/t/c/g)
# think about sequences with additional nucleotide codes (e.g. u, r, y, n etc.)
print("Sequence only:", DNA_seq)

# count nucleotides in sequence and print out 'GC content' (proportion of sequence comprised of C and G)
g_cnt = DNA_seq.count('G')
c_cnt = DNA_seq.count('C')
t_cnt = DNA_seq.count('T')
a_cnt = DNA_seq.count('A')
gc_cont = (g_cnt + c_cnt) / len(DNA_seq)
# ^ .count works fine in this case because the number of characters counted is few and the patterns is simple
# would consider regex if pattern got more complicated and created function if performing counts of more than 4 patterns
print("GC content = %.2f" %gc_cont)

# reverse the sequence using .reverse()
# annoying way to do this, but could be defined as a function if needed to use repeatedly
seq_list = list(DNA_seq)
seq_list.reverse()
rev_seq = ''.join(seq_list)

print("Reversed sequence:", rev_seq)

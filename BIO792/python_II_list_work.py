#!/usr/bin/env python3

# some basic list manipulation following 2. in assignment
# starting sequence (a string with characters separated by commas)
DNA_Seq = 'A,C,G,T,A,A,A,T,G,C,C,A,T,G,C,C,G,G,A,A,T,C,G,A,T,T,T'

# convert the string to list of the nucleotides only
# from assignement "Note that if you try to use list() to convert the string to a list, you would end up with commas as additional list elements"
# but ^ is not true?? play with print statements below to see...
dna_list = list(DNA_Seq.split(","))
# print(dna_list)
print("The first element in the list is", dna_list[0], "which should have no commas around it")
# print(DNA_Seq)

# convert the list back into a string with .join
orig_str = ','.join(dna_list)
print("The two following lines should be identical:\n %s\n %s" %(orig_str, DNA_Seq))

# adding in a second list, concatenating to the first, then cutting to the first 10 bases
SeqList2 = ['A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T','A','T']
comb_list = dna_list + SeqList2 # concatenating
first_ten_bs = comb_list[0:10] 

print("Length of the combined list is: %i\nLength of the 'first ten bases' list is: %i" %(len(comb_list), len(first_ten_bs)))
print(first_ten_bs) # checking contents

# example if/else function that prints the length of a list with statemnet confirming which part of the conditional it satisfies
def print_list(list):
    if len(list) <= 8:
        print("This list is shorter than 8, no length printed")
    elif len(list) <=16:
        print("This list has more than 8 elements but fewer than 17. Its length is %i" %(len(list)))
    else:
        print("This list has more than 16 elements. Its exact length is %i" %(len(list)))

# testing print_list() function on lists of various lengths
print_list(comb_list)
print_list(first_ten_bs)
short_list = comb_list[0:5]
print_list(short_list)

# printing the 'final list' (first_ten_bps) in reversed order
first_ten_bs.reverse()
print("The first 10 bases list reversed looks like:\n", first_ten_bs)
#!/usr/bin/env python3

# simple script to calculate Hardy Weinberg Equilibrium frequencies from a given frequency of the 'p' allele
while True:
    try:
        p_freq = float(input("'p' allele frequency: "))
    except ValueError:
        print("Not valid input. Need a number on scale 0-1")
        continue
    
    if p_freq > 1 or p_freq < 0:
        print("Number must be on scale 0-1")
        continue
    else:
        q_freq = 1-p_freq
        p_hom = p_freq**2
        q_hom = q_freq**2
        pq_het = 2*p_freq*q_freq
        print("Predicted genotype frequencies:\n  Homozygous p: %.2f\n  Homozygous q: %.2f\n  Heterozygous pq: %.2f" %(p_hom, q_hom, pq_het))
        break
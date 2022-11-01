#!/usr/bin/env python3

Team = "lakers"
Seq_one = "actgaaa"
Seq_two = "ATCGAA"
Seq3 = 'atcGGGC'

test_var = Seq_one.replace("a","_0_", 2)
type1 = type(test_var)
print(test_var, "Type:", type1)

P=38
A=10
R=16
print("%.3f points\n%.1f assists\n%s rebounds for Lebron" %(P, A, R), type(R))
# will print" 38 points, 10 assists, 16 rebounds for Lebron

s1 = "test"

long = s1 * 3
print(long)
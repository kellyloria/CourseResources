#!/usr/bin/env python3

# Goal: Using a for loop, print each value, a comma, the value multiplied by 2, a comma,
# the element that value occupies in the list, a comma, and whether the original number is even or odd

# starting list of integers 1-100
NumList=list(range(1,101))
ctr = 0
for num in NumList:
    if num%2 == 0:
        print("%i, %i, %i, even" %(num, num*2, ctr))
    else:
        print("%i, %i, %i, odd" %(num, num*2, ctr))
    ctr += 1
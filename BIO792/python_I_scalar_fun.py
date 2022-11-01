#!/usr/bin/env python3

# initializing some 'baseline' variables to make resetting of modified variables easy
def reset():
    global i1, i2, i3, f1, f2, s1, s2
    i1 = 8
    i2 = 22
    i3 = 103
    f1 = 7.8832
    f2 = 22.4
    s1 = "tuna"
    s2 = "dirt dog"

reset()

# just for FUN (hehe...) let's also write a little function to make output from type() prettier
def readable_type(var):
    return str(type(var)).split("'")[1].upper()

# += operator
# modifies the variable in place! (i.e. it has been changed from its initialized value, NOT a creation of new variable)
# mathematic addition if dealing with integers or floats, concatenation if dealing with strings
print("The initial s1 is:", s1, "\n", "The initial s2 is:", s2)
s1 += s2 
print("The result of s1 += s2:", s1)
reset()

# what about adding other strings not defined in a variable?
# (first reset variables)
s1 += " is a "
s1 += s2
print("s1 += some string I wrote += s2 now looks like:", s1)
reset()

# += will NOT work with strings and numbers, but you can force the number to be read as a string if you like
s1 += str(i1)
print("s1 and i1 (as a string) joined is:", s1)
i1_type = readable_type(i1)
print("And just to show that i1 itself has not been modified, its type is:", i1_type)
reset()

# what about numbers?
i1 += i2
print("i1 (8) += i2 (22) is equal to:", i1)
reset()

# are floats and integers compatible? (yes...)
# NOTE: math between an integer and a float always creates a float
i1 += f1
print("Doing += with an integer and float (i1 += f1) also works:", i1)
i1_type = readable_type(i1)
print("However, i1 should now by of type float. Its type is:", i1_type)
reset()

# a few other examples to show how -=, *=, and /= work
# *= WILL work with an input string as long as it is multiplied by an integer (creates a string repeated x times)
s1 *= 2
print("s1 *= 2 makes s1 now:", s1)
reset()
s1 *= i1
print("s1 *= i1 (8) makes s1 now:", s1)
reset()

# more math examples (all just logical extensions...)
i1 /= f1
i1_type = readable_type(i1)
print("Division of i1/f1, i1 now =", i1, "and is of type", i1_type)


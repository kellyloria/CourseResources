#!/usr/bin/env python3

# Goal: take an input string (x) and input integer (y) and output the string x repeated y times
# While we're at it, let's practice a while loop to keep people that wanna input obnoxious values at bay

while True:
    user_string = str(input("Give me a string, any string you want: "))
    if len(user_string) > 50:
        print("I know I said any string, but c'mon we've all got places to be. Try something shorter...")
        continue
    elif len(user_string) > 10:
        print("I'll accept it, but you better not be thinking of any big numbers with a string that long!")
        while True:
            try:
                user_int = int(input("Give me a whole number (and don't get crazy on me): "))
            except ValueError:
                print("Whole numbers only!")
                continue

            if len(user_string) * user_int > 1000:
                print("I said no big numbers with a string that long! Try less...")
                continue
            else:
                output = user_string * user_int
                print("You wanted", "'"+user_string+"'", "repeated", user_int, "times. Here's what that looks like:", "\n"+output)
                break
        break
    else:
        print("Your tendency towards brevity is appreciated!")
        while True:
            try:
                user_int = int(input("Give me a whole number (and don't get crazy on me): "))
            except ValueError:
                print("Whole numbers only!")
                continue

            if len(user_string) * user_int > 1000:
                print("Your short string was nice, but now your number is too large! Try something smaller...")
                continue
            else:
                output = user_string * user_int
                print("You wanted", "'"+user_string+"'", "repeated", user_int, "times. Here's what that looks like:", "\n"+output)
                break
        break

# Limitations/imperfections (logic exercise in thinking how this could be polished based on other purpose)
# Negative integers would be accepted but would lead to empty output
# No option to go back and change string if string+integer character limit is reached (can ONLY change integer)
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
# letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2

def swap_case(s):
    caps_string = ""
    for char in s:
        if char.isupper():
            caps_string += char.lower()
        else:
            caps_string += char.capitalize()
    return caps_string


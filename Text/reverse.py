"""
Reverse a String - Enter a string and the program
will reverse it and print it out.
"""

def checkReverse(s):
    if (s == s[::-1]):
        return True
    else:
        return False

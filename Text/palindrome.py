"""
Check if Palindrome - Checks if the string entered
by the user is a palindrome. That is that it reads
the same forwards as backwards like "racecar"
"""

def palindrome(s):
    i = 0;
    j = len(s) - 1
    while (i < j):
        if (s[i] == s[j]):
            i += 1
            j -= 1
        else:
            return False
    return True

print(palindrome('racecar'))

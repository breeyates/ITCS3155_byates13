# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
    three = n.count('3')
    six = n.count('6')
    nine = n.count('9')

    d = {3: three, 6: six, 9: nine}

    return max(d, key=lambda k: d[k])


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
    d = {c: 1 for c in s}

    for c in range(len(s) - 1):
        if s[c] == s[c + 1]:
            d[s[c]] += 1

    temp = max(d.values())

    return [key for key, value in d.items() if value == temp]


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    value = False

    for i in range(0, len(s) - 1):
        s.replace(" ", "")
        s = s.lower()

    if s == s[0:-1]:
        value = True

    return value

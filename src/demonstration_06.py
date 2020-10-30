"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

vowels = ['a', 'e', 'i', 'o', 'u']
def get_count(input_str):
    a = [i.lower() in vowels for i in input_str]
    b = len([i for i in a if i is True])
    return b



print(get_count('I am hello woraaald'))


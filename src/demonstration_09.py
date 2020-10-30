"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    leng= len(input_str)
    if leng % 2 == 0:
        idx = int(leng/2)
        return input_str[idx-1:idx+1]
    else:
        idx = int(leng//2)
        return input_str[idx]


print(get_middle("matoter"))


"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""
# plan
'''

'''

def last(a, n):
    # Check if n > len(a)
    if n > len(a):
        # return invalid
        return "invalid"
    
    # Check if it's an empty list:
    if n == 0:
        #return n == 0
        return []

    # otherwise:
    else:
        # return list from n to last
        return a[len(a)-n:]

print(last([4, 3, 9, 9, 7, 6], 3))
b = [1, 2, 3, 4, 5]
print (b[3:9])
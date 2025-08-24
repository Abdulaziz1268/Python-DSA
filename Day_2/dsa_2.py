# Second larges element

# the hard way
def second_largest(arr):
    y = 0
    z = 0
    for x in arr:
        if x > y:
            z = y
            y = x
    return z

# the clever way
def second_largest_element(arr):
    arr = list(set(arr)) # first converts arr to set to remove duplicate then convets it back to list b/c set don't support indexing.
    arr.sort()
    return arr[-2] if len(arr) >= 2 else None

arr = [1, 2, 3, 4, 5, 6]
print(second_largest(arr)) 
print(second_largest_element(arr))   
    
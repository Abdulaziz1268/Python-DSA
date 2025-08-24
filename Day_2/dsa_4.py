# Rotate an array to the right by one position
# the hard way
def rotate_arr(arr):
    arr1 = arr[len(arr) - 1]
    arr.pop()
    arr.insert(0, arr1)
    return arr

# the clever way
def rotate_by_one(arr):
    return [arr[-1]] + arr[:-1]   # creates a list with the last element of the arr then concatinates the rest to it

arr = [1, 2, 3, 4, 5]
print(rotate_arr(arr))
print(rotate_by_one(arr))

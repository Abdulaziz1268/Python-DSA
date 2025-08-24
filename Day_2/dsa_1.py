# Sum of array
def sum_arr(arr):
    y = 0
    for x in arr:
        y += x
    return y

arr = [1, 2, 3, 4, 5]
print(sum_arr(arr))
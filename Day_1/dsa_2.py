# find maximum in the array
def maximum(arr):
    m = arr[0]
    for x in arr:
        if x > m:
            m = x
    return m

print(maximum([1,6,3,5]))
        
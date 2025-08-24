# Cont Even & Odd Numbers
def count(arr):
    odd = even = 0
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return odd, even

arr = [1, 2, 3, 4, 5]
print(count(arr)) 
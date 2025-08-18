# this is the hard way
def reverse_string(s):
    rev = []
    leng = len(s)
    count = 1
    for x in s:
        rev.append(s[leng - count])
        count += 1
    return ''.join(rev)

# this is the simple way
def reverseString(s):
    return s[::-1]

print(reverse_string('hello'))
print(reverseString('hello'))
# check palindrome
# the hard way
def palindrome(s):
    rev = s[::-1]
    if rev == s:
        return 'is'
    else: return 'is not'

# the easy way
def is_palindrome(s):
    return s == s[::-1]

word = input('input the word to check if it\'s palindrome\n')
print(f'the word {palindrome(word)} palindrome')
print(is_palindrome(word))
def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

# Example
print(is_palindrome(121))  # Output: True
print(is_palindrome("racecar"))  # Output: True


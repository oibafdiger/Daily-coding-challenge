def palindrome_locator(s):
    if s != s[::-1]:
        return "none"
    
    mid = len(s) // 2

    if len(s) % 2 == 0:
        return s[mid - 1] + s[mid]
    else:
        return s[mid]


'''
Palindrome Characters
Given a string, determine if it's a palindrome and return the middle character (if it's odd length) or middle two characters (if it's even).

A palindrome is a string that is the same forward and backward.
If it's not a palindrome, return "none".
Tests:
Waiting:1. palindrome_locator("racecar") should return "e".
Waiting:2. palindrome_locator("level") should return "v".
Waiting:3. palindrome_locator("freecodecamp") should return "none".
Waiting:4. palindrome_locator("noon") should return "oo".
Waiting:5. palindrome_locator("11100111") should return "00".
'''

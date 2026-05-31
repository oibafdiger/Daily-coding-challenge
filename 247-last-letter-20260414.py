def get_last_letter(s):
    word = s.lower()
    last = 0
    index = 0
    for i, c in enumerate(word):
        if c.isalpha():
            if last < ord(c):
                last = ord(c)
                index = i
    return s[index]

print(get_last_letter("world"))

'''
Last Letter
Given a string, return the letter from the string that appears last in the alphabet.

If two or more letters tie for the last in the alphabet, return the first one.
Ignore all non-letter characters.
Tests:
Passed:1. get_last_letter("world") should return "w".
Passed:2. get_last_letter("Hello World") should return "W".
Passed:3. get_last_letter("The quick brown fox jumped over the lazy dog.") should return "z".
Passed:4. get_last_letter("HeLl0") should return "L".
Passed:5. get_last_letter("!#$ er@R asd fT.,> 2t0e9") should return "T".
'''



import string

def get_word_score(word):
    alphabet_positions = {char: index + 1 for index, char in enumerate(string.ascii_letters)}
    word_lower = list(word.lower())
    result = 0
    for char in word_lower:
        print(alphabet_positions[char])
        result += (alphabet_positions[char] if char.isalpha() else 0)
    print(result)
    return result

get_word_score("hello")

'''
Word Score
Given a word, return its score using a standard letter-value table:

Letter	Value
A	1
B	2
...	...
Z	26
Upper and lowercase letters have the same value.
Tests:
Passed:1. get_word_score("hi") should return 17.
Passed:2. get_word_score("hello") should return 52.
Passed:3. get_word_score("hippopotamus") should return 169.
Passed:4. get_word_score("freeCodeCamp") should return 94.

'''


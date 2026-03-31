def convert_words(s):
    list_words = s.split(" ")
    result = " ".join(str(len(word)) for word in list_words)
    return result

print(convert_words("hello world"))


'''
Word Length Converter
Given a string of words, return a new string where each word is replaced by its length.

Words in the given string will be separated by a single space
Keep the spaces in the returned string.
For example, given "hello world", return "5 5".

Tests:
Passed:1. convert_words("hello world") should return "5 5".
Passed:2. convert_words("Thanks and happy coding") should return "6 3 5 6".
Passed:3. convert_words("The quick brown fox jumps over the lazy dog") should return "3 5 5 3 5 4 3 4 3".
Passed:4. convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl") should return "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4".
'''

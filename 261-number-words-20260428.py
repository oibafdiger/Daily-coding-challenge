def get_number_words(n):
    result = ""
    unique_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
    multiples = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety",
    }
    
    if n <= 19:

        result = unique_numbers[n]
    else:
        result = multiples[n//10]

        if n%10 != 0:
            result += "-"+unique_numbers[n%10]

    print(result)
    return result

get_number_words(53)


'''
Number Words
Given an integer from 0 to 99, return its English word representation.

0 returns "zero".
Numbers 1-19 have unique names ("one", "two", ..., "ten", "eleven", ..., "eighteen", "nineteen").
Multiples of 10 from 20-90 have their own names ("twenty", "thirty", ..., "eighty", "ninety").
Numbers 21-99 that are not multiples of 10 are written as two words joined by a hyphen. For example "forty-two" and "fifty-three".
Tests:
Passed:1. get_number_words(0) should return "zero".
Passed:2. get_number_words(10) should return "ten".
Passed:3. get_number_words(19) should return "nineteen".
Passed:4. get_number_words(30) should return "thirty".
Passed:5. get_number_words(53) should return "fifty-three".
Passed:6. get_number_words(7) should return "seven".
Passed:7. get_number_words(12) should return "twelve".
Passed:8. get_number_words(60) should return "sixty".
Passed:9. get_number_words(67) should return "sixty-seven".
Passed:10. get_number_words(98) should return "ninety-eight".
'''

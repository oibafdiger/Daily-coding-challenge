def convert_parsecs(parsecs):

    return parsecs * 2 if parsecs % 2 else parsecs * 6 / 2

print(convert_parsecs(14))


'''
Parsec Converter
In a distant galaxy, parsecs are used to measure both time and distance. Given an integer number of parsecs, return its equivalent in time or distance.

If the given integer is odd, it represents time. If it's even, it represents distance.
Use these conversion rates:

Parsecs	Time/Distance
1	2 hours
2	6 light years
Return the converted value as an integer.

Tests:
Passed:1. convert_parsecs(1) should return 2.
Passed:2. convert_parsecs(2) should return 6.
Passed:3. convert_parsecs(31) should return 62.
Passed:4. convert_parsecs(88) should return 264.
Passed:5. convert_parsecs(17) should return 34.
Passed:6. convert_parsecs(14) should return 42.

'''

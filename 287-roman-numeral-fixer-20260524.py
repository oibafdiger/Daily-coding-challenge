def fix_numerals(s):
    values = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }

    # Step 1: sum malformed additive notation
    total = sum(values[ch] for ch in s)

    # Step 2: convert to standard Roman numerals
    roman_map = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, symbol in roman_map:
        while total >= value:
            result.append(symbol)
            total -= value

    return "".join(result)

print( fix_numerals("IIIILX"))


"""
Roman Numeral Fixer
Given a string of malformed Roman numerals, return the value in standard Roman numeral notation.

The input will only use additive notation, so each symbol adds its value to the total. As a reminder, here are the symbols and values:

Symbol	Value
"I"	1
"V"	5
"X"	10
"L"	50
"C"	100
"D"	500
"M"	1000
When re-encoding, use the largest possible symbol at each step, using subtractive pairs ("IV", "IX", "XL", "XC", "CD", "CM") where needed.

Tests:
Passed:1. fix_numerals("XIIIII") should return "XV".
Passed:2. fix_numerals("IIIILX") should return "LXIV".
Passed:3. fix_numerals("XXVVVIIIII") should return "XL".
Passed:4. fix_numerals("MDCCLXXXXVIIII") should return "MDCCXCIX".
Passed:5. fix_numerals("IIIIVVVVXXXXLLLLCCDD") should return "MCDLXIV".
Passed:6. fix_numerals("ILCDMIVDIIXLCVCXDL") should return "MMCMLXXXIV".
"""

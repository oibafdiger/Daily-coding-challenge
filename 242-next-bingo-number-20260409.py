def get_next_bingo_number(n):
    dic = ["B","I","N","G","O"]
    char = n[0]
    number = int(n[1:])

    number += 1
    if number > 75:
        number = 1
    char = dic[number // 15]


    return char + str(number)


print(get_next_bingo_number("B10"))


'''
Next Bingo Number
Given a bingo number, return the next bingo number sequentially.

A bingo number is a single letter followed by a number in its range according to this chart:

Letter	Number Range
"B"	1-15
"I"	16-30
"N"	31-45
"G"	46-60
"O"	61-75
For example, given "B10", return "B11", the next bingo number. If given the last bingo number, return "B1".

Tests:
Passed:1. get_next_bingo_number("B10") should return "B11".
Passed:2. get_next_bingo_number("N33") should return "N34".
Passed:3. get_next_bingo_number("I30") should return "N31".
Passed:4. get_next_bingo_number("G60") should return "O61".
Passed:5. get_next_bingo_number("O75") should return "B1".
'''

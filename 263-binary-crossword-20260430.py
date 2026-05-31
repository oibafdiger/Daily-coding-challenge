def is_in_crossword(char):

    cross = [
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0]
]
    char_in_bin = bin(ord(char))[2:].zfill(8)
    #char_in_bin = f"{ord(char):08b}"
    
    # Wandel string in int list
    int_list = list(map(int, char_in_bin))
    for row in cross:
        if int_list == row:
            print(True)
            return True
        elif int_list.reverse() == row:
            print(True)
            return True
    
    for col in range(8):
        # Extrahiere Spalte als Liste
        column = [cross[row] [col] for row in range(8)]
        if int_list == column:
            print(True)
            return True
        elif int_list.reverse() == column:
            print(True)
            return True
        
    
    print(False)
    return False

is_in_crossword("I")

'''
Binary Crossword
Given a character, determine if its 8-bit binary representation can be found in the following grid, horizontally or vertically in either direction:

0 1 0 0 0 0 0 1
0 1 1 0 1 1 1 1
0 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1
0 1 0 1 0 0 1 0
0 1 0 1 0 1 0 0
0 1 1 0 1 0 0 0
1 0 1 0 1 1 1 0
For example, "A" has the binary representation 01000001, which appears in the first row from left to right.

Tests:
Passed:1. is_in_crossword("I") should return True.
Passed:2. is_in_crossword("D") should return True.
Passed:3. is_in_crossword("0") should return True.
Passed:4. is_in_crossword("u") should return True.
Passed:5. is_in_crossword("Y") should return False.
Passed:6. is_in_crossword("p") should return False.
Passed:7. is_in_crossword("1") should return False.
Passed:8. is_in_crossword("Q") should return False.

'''

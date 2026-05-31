def is_narcissistic(n):
    liste_int = list(str(n))
    list_int_len = len(liste_int)
    result = 0
    for i in liste_int:
        result += int(i) ** list_int_len
        
    print(result, "=", n)
    return result == n


def is_narcissistic(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n

'''
Narcissistic Number
Given a positive integer, determine whether it is a narcissistic number.

A number is narcissistic if the sum of each of its digits raised to the power of the total number of digits equals the number itself.
For example, 153 has 3 digits, and 13 + 53 + 33 = 153, so it is narcissistic.

Tests:
Passed:1. is_narcissistic(153) should return True.
Passed:2. is_narcissistic(154) should return False.
Passed:3. is_narcissistic(371) should return True.
Passed:4. is_narcissistic(512) should return False.
Passed:5. is_narcissistic(9) should return True.
Passed:6. is_narcissistic(11) should return False.
Passed:7. is_narcissistic(9474) should return True.
Passed:8. is_narcissistic(6549) should return False.
'''

def is_fizz_buzz(arr):
    ok = True

    # Startwert finden
    for i in range(len(arr)):
        if isinstance(arr[i], int):
            start = arr[i] - i
            break

    for i in range(len(arr)):
        num = start + i

        if num % 15 == 0:
            if arr[i] != "FizzBuzz":
                ok = False
        elif num % 3 == 0:
            if arr[i] != "Fizz":
                ok = False
        elif num % 5 == 0:
            if arr[i] != "Buzz":
                ok = False
        else:
            if arr[i] != num:
                ok = False

    return ok

'''
FizzBuzz Validator
Given an array of sequential integers, with multiples of 3 and 5 replaced, determine if it's a valid FizzBuzz sequence.

In a valid FizzBuzz sequence:

Multiples of 3 are replaced with "Fizz".
Multiples of 5 are replaced with "Buzz".
Multiples of both 3 and 5 are replaced with "FizzBuzz".
All other numbers remain as integers.
Tests:
Passed:1. is_fizz_buzz([1, 2, "Fizz", 4, "Buzz"]) should return True.
Passed:2. is_fizz_buzz([13, 14, "FizzBuzz", 16, 17]) should return True.
Passed:3. is_fizz_buzz([1, 2, "Fizz", 4, 5]) should return False.
Passed:4. is_fizz_buzz(["FizzBuzz", 16, 17, "Fizz", 19, "Buzz"]) should return True.
Passed:5. is_fizz_buzz([1, 2, "Fizz", "Buzz", 5]) should return False.
Passed:6. is_fizz_buzz([97, 98, "Buzz", "Fizz", 101, "Fizz", 103]) should return False.
Passed:7. is_fizz_buzz(["Fizz", "Buzz", 101, "Fizz", 103, 104, "FizzBuzz"]) should return True.
'''

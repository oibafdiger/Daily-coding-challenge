def guess_number(secret, guess):
    if guess > secret:
        return "lower"
    elif guess < secret:
        return "higher"
    else:
        return "you got it!"

"""
Secret Number
Given a secret number and a guess, determine if the guess is correct.

Return:

"higher" if the secret number is higher than the guess.
"lower" if the secret number is lower than the guess.
"you got it!" if the guess is correct.
Tests:
Passed:1. guess_number(50, 30) should return "higher".
Passed:2. guess_number(85, 99) should return "lower".
Passed:3. guess_number(2026, 2026) should return "you got it!".
Passed:4. guess_number(92904, 11283) should return "higher".
Passed:5. guess_number(230495, 423920) should return "lower".
Passed:6. guess_number(120349, 120349) should return "you got it!".
"""

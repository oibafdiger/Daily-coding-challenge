def detect_roast(beans):
    score = []
    for char in beans:
        if char == "'":
            score.append(1)
        elif char == "-":
            score.append(2)
        else:
            score.append(3)

    avg = sum(score) / len(score)

    if avg < 1.75:
        return "Light"
    elif avg <= 2.5:
        return "Medium"
    else:
        return "Dark"

"""
Coffee Roast Detector
Given a string representing the beans used to make a cup of coffee, determine the roast of the cup.

The given string will contain the following characters, each representing a type of bean:

An apostrophe (') is a light roast bean worth 1 point each.
A dash (-) is a medium roast bean worth 2 points each.
A period (.) is a dark roast bean worth 3 points each.
The roast level is determined by the average of all the beans.

Return:

"Light" if the average is less than 1.75.
"Medium" if the average is 1.75 to 2.5.
"Dark" if the average is greater than 2.5.
Tests:
Passed:1. detect_roast("''-''''''-'-''--''''") should return "Light".
Passed:2. detect_roast(".'-''-''..'''.-.-''-") should return "Medium".
Passed:3. detect_roast("--.''--'-''.--..-.--") should return "Medium".
Passed:4. detect_roast("-...'-......-..-...-") should return "Dark".
Passed:5. detect_roast(".--.-..-......----.'") should return "Medium".
Passed:6. detect_roast("..-..-..-..-....-.-.") should return "Dark".
Passed:7. detect_roast("-'-''''''..-'.''-'.'") should return "Light".
"""

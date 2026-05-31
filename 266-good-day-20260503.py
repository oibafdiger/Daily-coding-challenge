def get_greeting(s):

    h,m = s.split(":")
    int_h = int(h)
    int_m = int(m)
    if 5 <= int_h < 12:
        return "Good morning"
    elif 12 <= int_h < 18:
        return "Good afternoon"
    elif 18 <= int_h < 22:
        return "Good evening"
    else:
        return "Good night"

print( get_greeting("06:30") )
print( get_greeting("12:00") )
print( get_greeting("21:59") )
print( get_greeting("00:01") )
print( get_greeting("11:30") )


'''
Good Day
Given a time string in "HH:MM" format (24-hour clock), return:

"Good morning" for times 05:00 to 11:59
"Good afternoon" for times 12:00 to 17:59
"Good evening" for times 18:00 to 21:59
"Good night" for times 22:00 to 04:59
Tests:
Passed:1. get_greeting("06:30") should return "Good morning".
Passed:2. get_greeting("12:00") should return "Good afternoon".
Passed:3. get_greeting("21:59") should return "Good evening".
Passed:4. get_greeting("00:01") should return "Good night".
Passed:5. get_greeting("11:30") should return "Good morning".

'''

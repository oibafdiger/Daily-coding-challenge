from datetime import datetime

def get_day_of_week(timestamp):

    weekday = datetime.fromtimestamp(timestamp / 1000).strftime("%A")
    print(weekday)
    return weekday

get_day_of_week(1775492249000)


'''
222-what-day-is-it-20260408.py
What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

Tests:
Passed:1. get_day_of_week(1775492249000) should return "Monday".
Passed:2. get_day_of_week(1766246400000) should return "Saturday".
Passed:3. get_day_of_week(33791256000000) should return "Tuesday".
Passed:4. get_day_of_week(1773576000000) should return "Sunday".
Passed:5. get_day_of_week(0) should return "Thursday".
'''

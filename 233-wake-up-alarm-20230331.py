def alarm_check(alarm_time, wake_time):

    alarm_time_h, alarm_time_m = map(int, alarm_time.split(":"))
    wake_time_h, wake_time_m = map(int, wake_time.split(":"))

    alarm_m = alarm_time_h *60 + alarm_time_m
    wake_m = wake_time_h *60 + wake_time_m

    if wake_m < alarm_m:
        return "early"
    elif alarm_m == wake_m or wake_m - alarm_m <= 10:
        return "on time"
    else:
        return "late"

print(alarm_check("07:00", "06:45"))

'''
Wake-Up Alarm
Given a string representing the time you set your alarm and a string representing the time you actually woke up, determine if you woke up early, on time, or late.

Both times will be given in "HH:MM" 24-hour format.
Return:

"early" if you woke up before your alarm time.
"on time" if you woke up at your alarm time, or within the 10 minute snooze window after the alarm time.
"late" if you woke up more than 10 minutes after your alarm time.
Both times are on the same day.

Tests:
Passed:1. alarm_check("07:00", "06:45") should return "early".
Passed:2. alarm_check("06:30", "06:30") should return "on time".
Passed:3. alarm_check("08:10", "08:15") should return "on time".
Passed:4. alarm_check("09:30", "09:45") should return "late".
Passed:5. alarm_check("08:15", "08:25") should return "on time".
Passed:6. alarm_check("05:45", "05:56") should return "late".
Passed:7. alarm_check("04:30", "04:00") should return "early".
'''

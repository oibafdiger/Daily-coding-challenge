from datetime import datetime, timedelta
def can_retake(finish_time, current_time):

    # Convert TimeStamp in ISOFormat
    finish_time_obj = datetime.fromisoformat(finish_time)
    current_time_obj = datetime.fromisoformat(current_time)
    # Calculate retake time by adding 48 hours to finish_time
    retake_time_obj = finish_time_obj + timedelta(hours=48)

    # Compare current time with retake time
    return current_time_obj >= retake_time_obj

print(can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00"))
print(can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00"))
print(can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00"))
print(can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59"))

"""
Cooldown Time
Given two timestamps, the first representing when a user finished an exam, and the second representing the current time, determine whether the user can take an exam again.

Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00". Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
Tests:
Passed:1. can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00") should return True.
Passed:2. can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00") should return False.
Passed:3. can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00") should return True.
Passed:4. can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59") should return False.
"""

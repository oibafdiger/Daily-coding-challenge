def get_direction(time1, time2):
    # Hilfsfunktion: Wandelt "HH:MM" in Minuten seit 00:00 um
    def to_minutes(t):
        h, m = map(int, t.split(":"))  # Stunden und Minuten extrahieren
        return h * 60 + m              # Gesamtminuten berechnen

    # Beide Zeiten in Minuten umwandeln
    t1 = to_minutes(time1)
    t2 = to_minutes(time2)

    # Vorwärts-Distanz:
    # Wie viele Minuten brauche ich, wenn ich auf der Uhr nach vorne gehe?
    # % (24*60) sorgt dafür, dass wir korrekt über Mitternacht springen
    forward = (t2 - t1) % (24 * 60)

    # Rückwärts-Distanz:
    # Wie viele Minuten brauche ich, wenn ich rückwärts gehe?
    backward = (t1 - t2) % (24 * 60)

    # Vergleich der beiden Richtungen
    if forward < backward:
        return "forward"   # Vorwärts ist schneller
    elif backward < forward:
        return "backward"  # Rückwärts ist schneller
    else:
        return "equal"     # Beide Richtungen gleich schnell


# Beispielaufruf
print(get_direction("10:00", "12:00"))

'''
Closest Time Direction
Given two times, determine whether you can get from the first to the second faster by moving forward or backward.

Times are given in 24-hour format ("HH:MM")
The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
Return:

"forward" if moving forward is shorter
"backward" if moving backward is shorter
"equal" if both directions take the same amount of time
Tests:
Passed:1. get_direction("10:00", "12:00") should return "forward".
Passed:2. get_direction("11:00", "05:00") should return "backward".
Passed:3. get_direction("00:00", "12:00") should return "equal".
Passed:4. get_direction("15:45", "01:10") should return "forward".
Passed:5. get_direction("03:30", "19:50") should return "backward".
Passed:6. get_direction("06:30", "18:30") should return "equal".
'''

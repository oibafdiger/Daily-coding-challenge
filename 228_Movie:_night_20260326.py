from datetime import datetime

def get_movie_night_cost(day, showtime, number_of_tickets):
    # Dienstag-Special: alle Tickets $5 
    if day == "Tuesday":
        return f"${5 * number_of_tickets:.2f}"

    # Basispreis nach Wochentag
    weekend = {"Friday", "Saturday", "Sunday"}
    price = 12 if day in weekend else 10

    # Uhrzeit in 24h umwandeln
    hour, minute = map(int, showtime[:-2].split(":"))
    period = showtime[-2:]
    if period == "pm" and hour != 12:
        hour += 12
    if period == "am" and hour == 12:
        hour = 0

    # Matinee-Rabatt vor 17:00 Uhr (außer Dienstag)
    if hour < 17:
        price -= 2

    # Gesamtkosten berechnen
    total = price * number_of_tickets
    return f"${total:.2f}"

print(get_movie_night_cost("Saturday", "10:00pm", 1))

"""
Movie Night
Given a string for the day of the week, another string for a showtime, and an integer number of tickets, return the total cost of the movie tickets for that showing.

The given day will be one of:

"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
"Sunday"
The showtime will be given in the format "H:MMam" or "H:MMpm". For example "10:00am" or "10:00pm".

Return the total cost in the format "$D.CC" using these rules:

Weekend (Friday - Sunday): $12.00 per ticket.
Weekday (Monday - Thursday): $10.00 per ticket.
Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays).
Tuesdays: all tickets are $5.00 each.
Tests:
Waiting:1. get_movie_night_cost("Saturday", "10:00pm", 1) should return "$12.00".
Waiting:2. get_movie_night_cost("Sunday", "10:00am", 1) should return "$10.00".
Waiting:3. get_movie_night_cost("Tuesday", "7:20pm", 2) should return "$10.00".
Waiting:4. get_movie_night_cost("Wednesday", "5:40pm", 3) should return "$30.00".
Waiting:5. get_movie_night_cost("Monday", "11:50am", 4) should return "$32.00".
Waiting:6. get_movie_night_cost("Friday", "4:30pm", 5) should return "$50.00".
Waiting:7. get_movie_night_cost("Tuesday", "11:30am", 1) should return "$5.00".
"""

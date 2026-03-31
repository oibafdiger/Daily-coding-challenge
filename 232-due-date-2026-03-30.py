from datetime import datetime
import calendar

def get_due_date(date_str):

    # String → datetime-Objekt umwandeln
    date = datetime.strptime(date_str, "%Y-%m-%d")

    # --- Monat und Jahr berechnen ---

    # Roh: Monate einfach addieren (kann > 12 werden)
    new_month = date.month + 9
    # Jahre berechnen, die durch den Monatsüberlauf entstehen
    # (new_month - 1) // 12 = wie viele volle Jahre stecken drin
    new_year = date.year + ( new_month -1) // 12

    # Monat wieder in den Bereich 1–12 bringen
    # % 12 gibt den Rest → +1, weil Monate bei 1 starten (nicht 0)
    new_month = (new_month -1) % 12 +1

    # --- Tag korrigieren ---

    # Letzten gültigen Tag im Zielmonat bestimmen
    # z.B. Februar → 28 oder 29, September → 30
    last_day = calendar.monthrange(new_year, new_month)[1]

    # Falls der ursprüngliche Tag zu groß ist (z.B. 31. Februar),
    # wird er auf den letzten gültigen Tag reduziert
    new_day = min(date.day, last_day)

    # --- Neues Datum zusammensetzen ---

    # Ersetzt Jahr, Monat und Tag im ursprünglichen Datum
    new_date = date.replace(year=new_year, month=new_month, day=new_day)

    # Ausgabe als String im gleichen Format
    return new_date.strftime("%Y-%m-%d")

print(get_due_date("2025-03-30"))

'''
Due Date
Given a date string, return the date 9 months in the future.

The given and return strings have the format "YYYY-MM-DD".
If the month nine months into the future doesn't contain the original day number, return the last day of that month.
Tests:
Passed:1. get_due_date("2025-03-30") should return "2025-12-30".
Passed:2. get_due_date("2025-04-27") should return "2026-01-27".
Passed:3. get_due_date("2025-05-29") should return "2026-02-28".
Passed:4. get_due_date("2026-06-30") should return "2027-03-30".
Passed:5. get_due_date("2026-10-11") should return "2027-07-11".
'''

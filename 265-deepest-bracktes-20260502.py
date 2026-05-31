def get_deepest_brackets(s):
    stack = []          # Stack speichert die geöffneten Klammern
    current = ""        # Buffer für den aktuellen Inhalt auf maximaler Tiefe
    max_depth = 0       # Maximale bisher erreichte Tiefe
    current_depth = 0   # Aktuelle Verschachtelungstiefe
    result = ""         # Ergebnis (Inhalt der tiefsten Klammern)

    opening = "([{"     # Alle öffnenden Klammern
    closing = ")]}"     # Alle schließenden Klammern

    # Mapping: welche schließende Klammer gehört zu welcher öffnenden
    matches = {')': '(', ']': '[', '}': '{'}

    for char in s:
        # FALL 1: Öffnende Klammer
        if char in opening:
            stack.append(char)     # Klammer auf den Stack legen
            current_depth += 1     # Tiefe erhöhen

            # Wenn wir eine neue maximale Tiefe erreichen:
            if current_depth > max_depth:
                max_depth = current_depth
                current = ""       # Buffer zurücksetzen (neuer tiefster Bereich)

        # FALL 2: Schließende Klammer
        elif char in closing:
            # Wenn wir gerade auf der maximalen Tiefe sind,
            # speichern wir den aktuellen Inhalt als Ergebnis
            if current_depth == max_depth:
                result = current

            stack.pop()            # Letzte öffnende Klammer entfernen
            current_depth -= 1     # Tiefe verringern

        # FALL 3: Normales Zeichen
        else:
            # Nur speichern, wenn wir uns genau auf der maximalen Tiefe befinden
            if current_depth == max_depth:
                current += char

    return result


'''
Deepest Brackets
Given a string containing balanced brackets, return the content of the deepest nested brackets.

Brackets can be any of the three types: (), [], and {}.
The input will always have a single deepest group.
For example, given "(hello (world))", return "world".

Tests:
Passed:1. get_deepest_brackets("(hello (world))") should return "world".
Passed:2. get_deepest_brackets("[outer [inner] outer]") should return "inner".
Passed:3. get_deepest_brackets("{a{b}c{d{e}f}g}") should return "e".
Passed:4. get_deepest_brackets("[the {quick (brown [fox] jumped) over (the) lazy} dog]") should return "fox".
Passed:5. get_deepest_brackets("f[(r)e{e}C{o[(d){e(C)}a]m}]p") should return "C".
'''

def get_best_hand(cards):
    # Rang und Farbe jeder Karte trennen
    ranks = [card[0] for card in cards]
    suits = [card[1] for card in cards]

    # Rang in Zahlenwert umwandeln (T=10, J=11, ..., A=14)
    order = "23456789TJQKA"
    values = sorted(order.index(rank) + 2 for rank in ranks)

    # Flush: Alle Karten haben dieselbe Farbe
    is_flush = len(set(suits)) == 1

    # Straight:
    # - Sonderfall A-2-3-4-5
    # - oder 5 verschiedene aufeinanderfolgende Werte
    is_straight = (
        values == [2, 3, 4, 5, 14] or
        (len(set(values)) == 5 and values[-1] - values[0] == 4)
    )

    # Anzahl gleicher Ränge bestimmen
    # Beispiel:
    # ["T","T","9","9","8"] -> [2,2,1]
    counts = sorted(
        [ranks.count(rank) for rank in set(ranks)],
        reverse=True
    )

    # Beste Hand von oben nach unten prüfen

    # 10-J-Q-K-A in derselben Farbe
    if is_flush and values == [10, 11, 12, 13, 14]:
        return "Royal Flush"

    # Straight + Flush
    if is_flush and is_straight:
        return "Straight Flush"

    # Vier Karten gleichen Rangs
    if counts == [4, 1]:
        return "Four of a Kind"

    # Drei gleiche + zwei gleiche
    if counts == [3, 2]:
        return "Full House"

    # Alle Karten gleiche Farbe
    if is_flush:
        return "Flush"

    # Fünf aufeinanderfolgende Werte
    if is_straight:
        return "Straight"

    # Drei Karten gleichen Rangs
    if counts == [3, 1, 1]:
        return "Three of a Kind"

    # Zwei verschiedene Paare
    if counts == [2, 2, 1]:
        return "Two Pair"

    # Genau ein Paar
    if counts == [2, 1, 1, 1]:
        return "Pair"

    # Keine besondere Kombination
    return "High Card"



# Tests
print(get_best_hand(["7s", "7h", "7d", "2c", "5h"]))
print( get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]))
print( get_best_hand(["2h", "5h", "7h", "9h", "Jh"]))
print( get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"])) 
print( get_best_hand(["Ts", "Th", "9d", "9c", "8h"])) 
print( get_best_hand(["9c", "8c", "7c", "6c", "5c"])) 
print( get_best_hand(["As", "Kh", "Jd", "8c", "5h"]))
print( get_best_hand(["As", "2h", "3d", "4c", "5h"])) 
print( get_best_hand(["Ts", "Th", "7c", "6d", "5h"])) 
print( get_best_hand(["As", "Ks", "Qs", "Js", "Ts"])) 


"""
Best Hand
Given an array of five strings representing playing cards, return the name of the best hand.

Each card is represented as a two-character string: the rank followed by the suit, "2h" for example.
Ranks, from low to high, are: "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", and "A".
Suits are: "h", "d", "c", and "s".
Aces ("A") can be used as high or low in a straight.
The hands, in order from worst to best, are:

Name	Description
"High Card"	No pair or better
"Pair"	Two of one rank
"Two Pair"	Two of one rank and two of another
"Three of a Kind"	Three of one rank
"Straight"	Five ranks in a row
"Flush"	Five of the same suit
"Full House"	Three of one rank, and two of another
"Four of a Kind"	Four of one rank
"Straight Flush"	Five ranks in a row of the same suit
"Royal Flush"	"A", "K", "Q", "J", "T" of the same suit
Return the name of the best hand.

Tests:
Passed:1. get_best_hand(["7s", "7h", "7d", "2c", "5h"]) should return "Three of a Kind".
Passed:2. get_best_hand(["Ks", "Kh", "Kd", "4s", "4h"]) should return "Full House".
Passed:3. get_best_hand(["2h", "5h", "7h", "9h", "Jh"]) should return "Flush".
Passed:4. get_best_hand(["As", "Ah", "Ad", "Ac", "Kh"]) should return "Four of a Kind".
Passed:5. get_best_hand(["Ts", "Th", "9d", "9c", "8h"]) should return "Two Pair".
Passed:6. get_best_hand(["9c", "8c", "7c", "6c", "5c"]) should return "Straight Flush".
Passed:7. get_best_hand(["As", "Kh", "Jd", "8c", "5h"]) should return "High Card".
Passed:8. get_best_hand(["As", "2h", "3d", "4c", "5h"]) should return "Straight".
Passed:9. get_best_hand(["Ts", "Th", "7c", "6d", "5h"]) should return "Pair".
Passed:10. get_best_hand(["As", "Ks", "Qs", "Js", "Ts"]) should return "Royal Flush".
"""

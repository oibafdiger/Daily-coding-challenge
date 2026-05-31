def get_cleanup_score(items):
    item_list = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }

    value = 0
    bonus = 0
    last_item = None

    for i, item in enumerate(items):
        
        # --- Rare Item ---
        if isinstance(item, list) and item[0] == "rare":
            item_value = item[1]
            bonus = 0
            last_item = None
        
        # --- Normales Item ---
        else:
            item_value = item_list[item]

            if item == last_item:
                bonus += 1
            else:
                bonus = 0

            item_value += bonus
            last_item = item

        # --- Multiplikator ---
        if (i + 1) % 5 == 0:
            multiplier = (i + 1) // 5 + 1
            item_value *= multiplier

        value += item_value

    return value

print(get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]))

'''
Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

Item	Base Value
"bottle"	10
"can"	6
"bag"	8
"tire"	35
"straw"	4
"cardboard"	3
"newspaper"	3
"shoe"	12
"electronics"	25
"battery"	18
"mattress"	38
A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

Streak bonus: If the same item appears consecutively, it gets increasing bonus points.

First consecutive occurrence: base value
Second: base value + 1
Third: base value + 2
etc.
Fifth Item Multiplier: Every fifth item collected gets a multiplier.

Fifth item: *2
Tenth item: *3
etc.
Apply the multiplier after calculating any bonuses.

Tests:
Passed:1. get_cleanup_score(["bottle", "straw", "shoe", "battery"]) should return 44.
Passed:2. get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) should return 58.
Passed:3. get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"]) should return 79.
Passed:4. get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]]) should return 358.
Passed:5. get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"]) should return 383.
'''

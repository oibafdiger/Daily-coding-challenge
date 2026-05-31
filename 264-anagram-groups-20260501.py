def group_anagrams(words):
    anagram_map = {}

    for word in words:
        # Sortiere die Buchstaben zum Erstellen des Schlüssels
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
        
        # Hinzufügen: Füge das Originalwort zur Liste des Schlüssels hinzu
        anagram_map[sorted_word].append(word)

    print(list(anagram_map.values()))
    return list(anagram_map.values())

group_anagrams(["listen", "silent", "hello", "enlist", "world"])

'''
Anagram Groups
Given an array of words, return a 2d array of the words grouped into anagrams.

Words are anagrams if they contain the same letters in any order.
Each word belongs to exactly one group.
Return order doesn't matter.
For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].

Tests:
Passed:1. group_anagrams(["listen", "silent", "hello", "enlist", "world"]) should return [["listen", "silent", "enlist"], ["hello"], ["world"]].
Passed:2. group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) should return [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]].
Passed:3. group_anagrams(["care", "race", "acre", "pots", "stop", "tops", "opts", "post", "spot", "evil", "vile", "live", "veil"]) should return [["acre", "care", "race"], ["evil", "live", "veil", "vile"], ["opts", "post", "pots", "spot", "stop", "tops"]].
Passed:4. group_anagrams(["algorithms", "logarithms", "education", "cautioned", "auctioned", "triangle", "integral", "alerting", "relating"]) should return [["alerting", "integral", "relating", "triangle"], ["algorithms", "logarithms"], ["auctioned", "cautioned", "education"]].
'''


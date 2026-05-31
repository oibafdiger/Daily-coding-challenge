
def get_oldest(people):

    people_names = []
    sorted_people = sorted(people, key=lambda x: x["age"], reverse=True)
    max_age = sorted_people[0]["age"]
    for person in sorted_people:
        if person["age"] == max_age:
            people_names.append(person["name"])
        else:
            break
    return people_names   

print(get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]))
'''
Oldest Person
Given an array of objects, each with a "name" and "age" property, return an array containing the name of the oldest person.

If multiple people share the oldest age, return all of their names in the order they appear in the input.

Tests:
Passed:1. get_oldest([{ "name": "Brenda", "age": 40 }]) should return ["Brenda"].
Passed:2. get_oldest([{ "name": "Alice", "age": 30 }, { "name": "Bob", "age": 25 }]) should return ["Alice"].
Passed:3. get_oldest([{ "name": "Allison", "age": 25 }, { "name": "Bill", "age": 30 }, { "name": "Carol", "age": 30 }]) should return ["Bill", "Carol"].
Passed:4. get_oldest([{ "name": "George", "age": 50 }, { "name": "Shirley", "age": 42 }, { "name": "Beth", "age": 48 }, { "name": "Holly", "age": 50 }, { "name": "Kevin", "age": 44 }, { "name": "Frank", "age": 47 }, { "name": "Zach", "age": 50 }, { "name": "Jennifer", "age": 43 }]) should return ["George", "Holly", "Zach"].

'''    




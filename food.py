from random import choice
food = choice(['apple','grape','steak','lamb'])

if food == "apple" or food == "grape":
    print("fruit")
elif food == "steak" or food == "lamb":
    print("meat")
else:
    print("Uhhh whats that?")

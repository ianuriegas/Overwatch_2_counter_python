import json

# Open the JSON file for reading
with open('heroes.json', 'r') as f:
    heroes = json.load(f)

# Ask for input of enemy team heroes
tank = input("Tank: ")
damage_1 = input("Damage 1: ")
damage_2 = input("Damage 2: ")
support_1 = input("Support 1: ")
support_2 = input("Support 2: ")

enemy_team = [tank, damage_1, damage_2, support_1, support_2]

# Count the number of times each counter appears
counter_counts = {}
for hero in enemy_team:
    counters = heroes[hero]["counters"]
    for counter in counters:
        if counter in counter_counts:
            counter_counts[counter] += 1
        else:
            counter_counts[counter] = 1

# Ask for input of user's role
user_role = input("What role are you playing? (Tank, Damage, or Support): ")

print("==========================================================")

# Output the counters in order from most to least common, filtered by user's role
print("Counters from best to least for " + user_role + " players:")
for counter, count in sorted(counter_counts.items(), key=lambda x: x[1], reverse=True):
    if heroes[counter]["role"].lower() == user_role.lower():
        print(counter + " - " + str(count) + " appearances")

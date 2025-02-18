#Katie Mackness
# 18/05/2024 - Updated 18/02/2025
# Python 3.11.4
# ----------------------------------------------------------
# Conditional Tests
# ----------------------------------------------------------

# Assign a point value depending on the color of an alien in a game
alien_color = 'green'

if alien_color == 'green':
    print("You won 5 points!")
elif alien_color == 'yellow':
    print("You won 10 points!")
elif alien_color == 'red':
    print("You won 15 points!")
else:
    print("Keep trying")

# Determine the stage of life of a person based on their age
def stages_of_life(name: str, age: int) -> None:
    if age < 2:
        print(f"{name} is a baby")
    elif age >= 2 and age < 4:
        print(f"{name} is a toddler")
    elif age >= 4 and age < 13:
        print(f"{name} is a kid")
    elif age >= 13 and age < 20:
        print(f"{name} is a teenager")
    elif age >= 20 and age < 65:
        print(f"{name} is an adult")
    elif age >= 65:
        print(f"{name} is an elder")

# "name of person": their age
people = {
    "Daria": 1, 
    "Robert": 2, 
    "Henert": 7, 
    "Philmert": 13, 
    "Gerberta": 20, 
    "Johnetta": 40, 
    "Sandretta": 65
    }

for name, age in people.items():
    stages_of_life(name, age)
import random

wheel = []

# Functions


def wheel_maker(empty_wheel):
    for i in range(1, 20):
        empty_wheel.append((random.randint(1, 10))*100)
    empty_wheel.insert(random.randint(1, 15), "Lose a Turn")

# def phrase_picker:


# Generate the wheel
wheel_maker(wheel)
print(wheel)

# Play the game
print("Welcome to WHEEL. OF. FORTUNE!!!!!!!")
while True:
    print("1: Spin the wheel")
    print("2: Buy a vowel")
    print("3: Solve the puzzle")
    print("4: Quit the game...you quitter...")
    x = input("What would you like to do? : ")
    if x == '4':
        input("Quitter")
        break
    else:
        print("Unregonized Command")

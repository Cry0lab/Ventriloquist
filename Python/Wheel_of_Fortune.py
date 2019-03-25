import random

wheel = []
players = {}
# Functions


def createPlayers():
    i = 1
    numberOfPlayers = int(input("How many players are going to be playing?"))
    while i <= numberOfPlayers:
        playerName = input("What is the name of Player " + str(i) + "?:  ")
        print(playerName)
        i += 1


def wheelMaker(empty_wheel):
    for i in range(1, 20):
        empty_wheel.append((random.randint(1, 10))*100)
    empty_wheel.insert(random.randint(1, 15), "Lose a Turn")
    empty_wheel.insert(random.randint(1, 15), "Bankrupt")


def spin(phrase, wheel):
    i = wheel[random.randint(0, len(wheel))]
    print(i)


# def phrase_picker:
guessPhrase = "This is the phrase"

# Generate the wheel
createPlayers()
wheelMaker(wheel)
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
    elif x == '1':
        spin(guessPhrase, wheel)
    else:
        print("Unregonized Command")

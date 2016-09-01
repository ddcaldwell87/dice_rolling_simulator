from random import randint

play = True

while play:
    roll = randint(1, 6)
    print roll
    answer = raw_input("Roll again? (y/n)")
    if answer == "y":
        play = True
    elif answer == "n":
        break
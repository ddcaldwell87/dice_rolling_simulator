from random import randint

play = True

while play:
    roll = randint(1, 6)
    print(roll)
    ask = True
    while ask:
        answer = input("Roll again? (y/n)")
        print(answer)
        if answer != "y" and answer != "n":
            print("Invalid Input")
        else:
            ask = False
    if answer == "y":
        play = True
    elif answer == "n":
        break
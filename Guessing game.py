import random
randomint = random.randint(1, 100)
x = int(input("Guess number(1-100) : "))

while True:
    if x == randomint:
        print("You are right")
        break
    elif x > randomint:
        print("Too high")
        x = int(input("Guess number(1-100) : "))
    else:
        print("Too low")
        x = int(input("Guess number(1-100) : "))
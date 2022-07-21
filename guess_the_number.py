import random
randnum = random.randint(1,50)
userguess  = None
guesses = 0
while (userguess != randnum):
    userguess = int(input("Enter your guess number"))
    guesses += 1
if input > randnum:
        print("You have entered smaller number,please enter greater number")
elif input < randnum:
        print("You have entered greater number,please enter smaller number")
else:
        print("Congrats you entered correct number")

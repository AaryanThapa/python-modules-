n =64
number_of_guesses = 1
print("You have only 9 number of limited guesses")
while(number_of_guesses<=9):
    guess_number = int(input("Enter a number:\n"))

    if guess_number > 64:
        print("You have entered large number try some smaller numbers:\n")
    elif guess_number < 64:
        print("You have entered small number try some larger numbers:\n")
    else:
        print("Congrats you have entered correct number\n")
        print(number_of_guesses,"Number of guesses you yook to finsih the game")
        break
    print(9-number_of_guesses,"Number of gusses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses >= 9):
    print("Game over")

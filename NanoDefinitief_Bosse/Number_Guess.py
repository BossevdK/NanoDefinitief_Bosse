import random
def number_guesser():
    print("\n--In this game you need to guess the number between 1 and 100, you get hints, but try to do it in the least guesses possible--")
    playing = True
    computer_guess = random.randrange(1, 100)
    while playing:
        #Makes the code repeat until the condition is met
        try:
            guess_count = 0 #Starts the count of the guesses
            user_guess = 0
            while user_guess != computer_guess:
                #Checks if the condition will be met and if the game should end
                user_guess = int(input("What is your guess?: "))
                if user_guess < computer_guess:
                    print("You need to guess higher")
                    guess_count += 1
                elif user_guess > computer_guess:
                    print("You need to guess lower")
                    guess_count += 1
                else:
                    print("Well done!")
                    print("You did it in:" + " " + str(guess_count + 1) + " " + "guesses!")
                    playing = False
        except ValueError: #Checks if the answer is allowed to be put in the answerbox
            print("There is something wrong with your guess, try again")


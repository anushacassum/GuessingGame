import random

number = random.randint(0, 10)
guess = int(input("Enter an integer from 0 to 10: "))
numofguesses = 0

while number != guess:
    print ("Sorry, try again!")
    numofguesses = numofguesses + 1
    if numofguesses = 5:
        hint = input(print ("Do you want a hint? Type y or n: "))
        if hint = 'y':
            if number>5:
                print("The number is greater than 5")
            elif number<5:
                print("The number is less than 5")
        if hint = 'n':
            guess = int(input("Enter an integer from 0 to 10: "))
    if numofguesses = 8:
        print("You have failed to guess the number")
        print("The number was : ", number)

if number = guess :
    print("Congratulations! You guessed the number in ", numofguesses "number of tries")
        

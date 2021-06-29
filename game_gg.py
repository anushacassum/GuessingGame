

import random
n=random.randint(0,10)
print("This is a guessing game where the user needs to guess a number from 0 to 10 inorder to win.")
print("")
print("The quicker the user guesses the number, the higher the number of points.")
print("")
print ("Following are the rules:")
print("> Maximum number of guesses would be 8.")
print("> After first 5 wrong tries, the user would be asked if they need a hint. ")
print("> If user needs a hint, they shall be provided with a hint:")
print(" - Even number or odd number")
print(" - Number is less than 5 or more than 5.")
print("> Game over if user is unable to guess at all.")
print("")
print("Points table:")
print("1 guess used: 15 points")
print("2 guesses used:13 points")
print("3 guesses used:11 points")
print("4 guesses used:9 points")
print("5 guesses used:7 points")
print("6 guesses used:5 points")
print("7 guesses used:3 points")
print("8 guesses used:1 point")
print("")
print("The score will be displayed in the end if the user has guessed the right number")

a=int(input("Please guess the number between -1 and 11:"))


b=1
while b<9:
    if a==n:
       print("Congratulations. You guessed the right number in", b, "guess(es).")
       if b==1:
           print("Your score is 15 points")
       if b==2:
           print("Your score is 13 points")
       if b==3:
           print("Your score is 11 points")
       if b==4:
           print("Your score is 9 points")
       if b==5:
           print("Your score is 7 points")
       if b==6:
           print("Your score is 5 points")
       if b==7:
           print("Your score is 3 points")
       if b==8:
           print("Your score is 1 point")
       b=10
    elif b<8:
       b+=1
       
       a=int(input("The number was not the correct one. Please guess some other number:"))
       print("Number of guesses used=", b)
    
    if a!=n and b==5:
       b+=1
       c=input("The number was not correct. Since its ur 6th try. Do u want a hint?")
       if c.upper()=="YES":
          if n % 2 ==0 and n /1 !=0 :
              print("The number is even")
          if n % 2 == 1:
              print("The number is odd")
       if c.upper()=="NO" :
            print("Ok sure")
       a=int(input("Please guess some other number:"))
       print("Number of guesses=", b)
    if a!=n and b==6:
        b+=1
        d=input("The number was not correct. Since its ur 7th try. Do u want a hint?")
        if d.upper()=="YES" :
            if n %3 ==0:
                print("The number is a multiple of 3")
            else:
                print("The number is not a multiple of 3")
        if d.upper()=="NO" :
            print("Ok sure")
        a=int(input("Please guess some other number:"))
        print("Number of guesses=", b)
    if a!=n and b==7:
        b+=1
        e=input("The number was not correct. Since its ur 8th try. Do u want a hint?")
        if e.upper()=="YES" :
            if n>5:
                print("The number is greater than 5")
            else:
                print("The number is lesser than or equal to 5")
        if e.upper()=="NO" :
            print("Ok sure")
        a=int(input("Please guess some other number:"))
        if a!=n:
            print("Number of guesses=", b)
    if a!=n and b==8:
          print("Sorry, but you have used all your guesses.Game over. Better luck next time")
          b+=1
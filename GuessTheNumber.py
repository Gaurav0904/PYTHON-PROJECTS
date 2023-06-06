#this is GuessTheNumber game

import random 
number = random.randint(1,15)

for guessestaken in range(1,6) :   
    print("Guess the number I am thinking(hint : between 0 and 10 ) ")
    guess = int(input())

    if guess < number :
        print("YOUR GUESS IS TOO LOW")
    elif guess > number :
        print("YOUR GUESS IS TOO HIGH")
    else :
        break #correct wali condition 

if guess == number :
    print("Awesome !! You guessed the number in "+str(guessestaken) + " guesses .")
else :
    print("YOU COULD NOT GUESS THE NUMBER CORRECTLY")
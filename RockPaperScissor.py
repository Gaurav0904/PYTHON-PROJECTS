# ROCK PAPER SCISSOR GAME

import sys , random 


print("ROCK PAPER SCISSOR ... ")


## Input Player's move 

while True :
    print("Enter (r)ock , (p)aper , (s)cissors or (q)uit .")
    playermove = input()

    if playermove == "q" :
        sys.exit()
    elif playermove == "r" or playermove == "p" or playermove == "s" or playermove == "q" :
        break 
    print("Type one of r, p, s or q")

## Generate Computer's move

randomnumber = random.randint(1,3)

if randomnumber == 1 :
    computermove = "r" 
    print(playermove + " versus Rock")

elif randomnumber == 2 :
    computermove = "p"
    print(playermove + " versus Paper")

elif randomnumber == 3 :
    computermove = "s" 
    print(playermove + " versus Scissors")

## Comparing the moves

if computermove == playermove :
    print("TIE !!")

elif computermove == "r" and playermove == "p" :
    print("WIN !!")

elif computermove == "r" and playermove == "s" :
    print("LOSS !!")

elif computermove == "p" and playermove == "s" :
    print("WIN !!")

elif computermove == "p" and playermove == "r" :
    print("LOSS !!")

elif computermove == "s" and playermove == "p" :
    print("LOSS !!")

elif computermove == "s" and playermove == "r" :
    print("WIN !!")
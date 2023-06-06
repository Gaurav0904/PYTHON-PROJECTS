import sys

try :

    def collatz(number) :
        if number%2 == 0 :
            print(number//2)
            return number//2
    
        elif number%2 == 1:
            print(3*number+1)
            return 3*number+1
        
    user = int(input("Enter an integer : "))
    
    while user != 1 :
        user = collatz(user)


    print("Finally 1 achieved !")


except ValueError :
    print("Please Enter an Integer !")
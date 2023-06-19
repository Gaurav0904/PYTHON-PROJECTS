# ask user a name and output their bday from the dictionary


birthday = {"Alice":"April 1","Bob":"April 25","Charles":"December 12"}


print("Enter a Name :\n")
while True :
    name = input()
    if name == "":
        break
    if name in birthday:
        print(name + "'s birthday is on " + birthday[name])
    else :
        print("Currently I don't have any information of that.\nAlthough you can add their birthday if you want :\n")
        print("y/n\n")
        opt = input()
        if opt == "y":
            bday = input()
            birthday[name] = bday
            print("Database Updated !!!")
            continue
        elif opt == "n":
            continue
        

        




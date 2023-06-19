cats = []

while True :
    catnames = input("Enter the names of your cats(or 'ENTER' to exit)\n")
    cats = cats + [catnames]
    if catnames == "":
        break
    
print("The names of your cats are :")
for catnames in cats :
    print(catnames)

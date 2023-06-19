list = []
print("Enter the items in list :\n")

while True :
    item = input()
    list = list + [item]

    if item == "" :
        break 



print("Following are the items i your list :")

for i in range(len(list)-1) :
    print('Item no.' + str(i+1)  + '-' + list[i])

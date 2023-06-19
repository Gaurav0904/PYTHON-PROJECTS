# create an empty list 
list1 = []


print("Enter the items below : \n")

# input the list items from user
while True :
    
    item = input()
    list1.append(item)
    if item == "" :
        break


l = len(list1)
print("length: ",l)

del list1[l-1]

#print out the list 
print(list1)

length = len(list1)
print("length: ", length )


print("Following is the conversion to string :\n")

for i in range(length-1):
    print(list1[i]+" , ", end = "")

print("and " + list1[length-1])

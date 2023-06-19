import copy

LIST = [1,2,3,4,5,6]

LIST1 = copy.copy(LIST)

print(LIST1)

LIST1.append(7)

print(LIST1)
print(LIST)

# copy() was used to create a different list at a different reference . If we had modified it without copy both lists would have been modified . 
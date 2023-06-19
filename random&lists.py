import random
list = ['1','2','3',"4", "5", "6", "7", "8","9","10"]


print(random.choice(list))

random.shuffle(list)
# list after randomly changing indices of the list items
print(list)

##  Using choice and shuffle functions from Random the module 
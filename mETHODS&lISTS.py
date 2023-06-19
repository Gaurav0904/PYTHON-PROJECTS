list = [1,2,3,4,5,6,7,8,9]
print(list.index(8))

list.append(10)
print(list)

list.insert(0,0)
print(list)

list.remove(0)
print(list)

temp = [-5,-8,3.14,1,6,2,1,7,8,45,68]
temp.sort()
print(temp)
temp.sort(reverse=True)
print(temp)
# For strings sort uses ACIIbetical order to avoid use key = str.lower in sort()


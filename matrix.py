matrix = []

for rows in range(3):
    r = []
    for columns in range(4):
        r.append(int(input()))
    matrix.append(r)

for rows in range(3):
    for columns in range(4):
        print(matrix[rows][columns] , end = "  ")
    print()

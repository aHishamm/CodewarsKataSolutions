def sum_diagonals(matrix):
    dig1 = 0
    dig2 = 0
    for i in range(0,len(matrix[0])):
        dig1 = dig1 + matrix[i][i]
    reverseCounter = 0
    for i in reversed(range(0,len(matrix[0]))):
        dig2 = dig2 + matrix[reverseCounter][i]
        reverseCounter += 1 
    return dig1+dig2
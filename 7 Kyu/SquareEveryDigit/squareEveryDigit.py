def square_digits(num):
    squaredig = '' 
    numString = list(str(num))
    for i in range(len(numString)):
        numString[i] = str(int(numString[i]) ** 2)
    numString = int("".join(numString)) 
    return numString
        
    
    
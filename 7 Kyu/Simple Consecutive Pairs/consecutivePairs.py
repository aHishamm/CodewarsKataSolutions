def pairs(ar):
    returnArr = []
    Count = 0
    if len(ar) % 2 == 0: 
        returnArr = [ar[i:i+2] for i in range(0,len(ar),2)]
        for i in range(len(returnArr)):  
            if returnArr[i][1] == returnArr[i][0]+1:
                Count += 1  
            elif returnArr[i][1] == returnArr[i][0]-1: 
                Count += 1 
        return Count
    elif len(ar) % 2 != 0: 
        returnArr = [ar[i:i+2] for i in range(0,len(ar),2)]
        for i in range(len(returnArr)-1):  
            if returnArr[i][1] == returnArr[i][0]+1:
                Count += 1  
            elif returnArr[i][1] == returnArr[i][0]-1: 
                Count += 1 
        return Count
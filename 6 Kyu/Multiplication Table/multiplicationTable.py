def multiplication_table(size):
    returnArr = []
    for i in range(1,size+1):
        returnInnerArr = []
        for k in range(1,size+1):
            returnInnerArr.append(k * i)
        returnArr.append(returnInnerArr)
    return returnArr
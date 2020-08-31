def filter_list(l):
    returnArr = []
    for i in range(len(l)):
        if type(l[i]) == int: 
            returnArr.append(l[i]) 
    return returnArr
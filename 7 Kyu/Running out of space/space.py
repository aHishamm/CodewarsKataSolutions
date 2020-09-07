def spacey(array):
    returnArr = []
    for i in range(1,len(array)+1):
        returnArr.append("".join(array[:i]))
    return returnArr
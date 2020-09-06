def split_by_value(k, elements):
    returnArr = []
    for i in range(len(elements)):
        if elements[i] < k:
            returnArr.append(elements[i])
    #returnArr.append(k)
    for i in range(len(elements)):
        if elements[i] >= k:
            returnArr.append(elements[i])
    return returnArr
def uniq(seq): 
    returnArr = []
    if seq == []: 
        return []
    returnArr.append(seq[0])
    if len(seq) < 2: 
        return seq
    for i in range(1,len(seq)):
        if seq[i] != seq[i-1]:
            returnArr.append(seq[i])
    return returnArr
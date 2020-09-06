def pluck(objs, name): 
    returnArr = []
    for i in range(len(objs)):
        if name in objs[i].keys(): 
            returnArr.append(objs[i][name])
        else:
            returnArr.append(None)
    return returnArr
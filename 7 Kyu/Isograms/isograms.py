def is_isogram(string):
    if string == "":
        return True
    stringCheck = []
    string = string.lower() 
    stringList = list(string)
    for i in range(len(stringList)):
        if stringList[i] in stringCheck:
            return False
        else: 
            stringCheck.append(stringList[i])
    return True
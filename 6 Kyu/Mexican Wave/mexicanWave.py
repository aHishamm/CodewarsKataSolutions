def wave(people):
    peopleLen = len(people)
    returnArr = []
    for i in range(0,peopleLen):
        peopleList = list(people)
        if peopleList[i] == ' ':
            continue
        peopleList[i] = peopleList[i].upper()
        returnArr.append("".join(peopleList))
    return returnArr
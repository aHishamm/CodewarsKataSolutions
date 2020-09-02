def word_pattern(word):
    word = word.lower() 
    wordList = list(word)
    dict = {}
    returnArr = []
    counter = 0 
    dict[wordList[0]] = counter
    returnArr.append(str(dict.get(wordList[0])))
    for i in range(1,len(wordList)):
        if wordList[i] in dict.keys():
            returnArr.append(str(dict.get(wordList[i])))
        else: 
            counter += 1
            dict[wordList[i]] = counter
            returnArr.append(str(counter))
    return ".".join(returnArr)
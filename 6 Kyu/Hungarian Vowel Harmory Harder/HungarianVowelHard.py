def instrumental(word):
    frontVowel = 'eéiíöőüű'
    backVowel = 'aáoóuú'
    VowelPairDict = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú', 'ö': 'ő', 'ü': 'ű'}
    digraphs = ['sz','zs','cs']
    # if word ends with a vowel
    returnArr1 = list(word) 
    if word[-1] in frontVowel:
        if word[-1] not in VowelPairDict.keys(): 
            returnArr1.append('vel')
        else: 
            returnArr1[-1] = VowelPairDict.get(word[-1])
            returnArr1.append('vel')
        print(returnArr1)
        return "".join(returnArr1)
    elif word[-1] in backVowel:
        if word[-1] not in VowelPairDict.keys(): 
            returnArr1.append('val')
        else:
            returnArr1[-1] = VowelPairDict.get(word[-1])
            returnArr1.append('val')
        print(returnArr1)
        return "".join(returnArr1)
    # if word ends with a constant 
    # 1: check for digraph 
    if word[-2:] in digraphs: 
        returnArr1[-2] = returnArr1[-2]+returnArr1[-2]
        for i in reversed(range(len(returnArr1))): 
            if returnArr1[i] in backVowel: 
                return "".join(returnArr1)+'al'
            elif returnArr1[i] in frontVowel: 
                return "".join(returnArr1)+'el'
    # 2: normal non-digraphs 
    returnArr1[-1] = returnArr1[-1]+returnArr1[-1]
    for i in reversed(range(len(returnArr1))): 
        if returnArr1[i] in backVowel: 
            return "".join(returnArr1)+'al'
        elif returnArr1[i] in frontVowel: 
            return "".join(returnArr1)+'el'
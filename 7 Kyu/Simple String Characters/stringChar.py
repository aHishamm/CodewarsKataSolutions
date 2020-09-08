def solve(s):
    returnArr = []
    specialChar = ',.\'\";-+=[@_!#$%^&*()<>?/\|}{~:]'
    #looping through the uppercase 
    sum = 0
    for i in range(len(s)):
        if s[i].isupper() == True: 
            sum += 1
    returnArr.append(sum)
    sum = 0 
    #looping through the lowercase 
    for i in range(len(s)):
        if s[i].islower() == True: 
            sum += 1
    returnArr.append(sum)
    sum = 0 
    #looping through the numbers 
    for i in range(len(s)):
        if s[i].isdigit() == True: 
            sum += 1
    returnArr.append(sum)
    sum = 0
    #looping through the special characters
    for i in range(len(s)):
        if s[i] in specialChar: 
            sum += 1
    returnArr.append(sum)
    return returnArr
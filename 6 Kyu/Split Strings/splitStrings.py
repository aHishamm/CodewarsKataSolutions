def solution(s):
    if s == '': return []
    returnArr = []
    if len(s) % 2 == 0: 
        returnArr = [s[i:i+2] for i in range(0, len(s), 2)] 
        return returnArr
    elif len(s) % 2 != 0: 
        returnArr = [s[i:i+2] for i in range(0, len(s), 2)] 
        returnArr[-1] = returnArr[-1]+'_'
        return returnArr
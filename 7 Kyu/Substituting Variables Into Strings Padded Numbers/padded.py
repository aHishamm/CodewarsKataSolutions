def solution(value):
    returnArr = ['0','0','0','0','0']
    value = list(str(value))
    value = value[::-1]
    for i in range(len(value)): 
        returnArr[0-(i+1)] = value[i] 
    return "Value is "+"".join(returnArr)
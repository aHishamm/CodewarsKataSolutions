def solution(roman):
    romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romanList = list(roman)
    romanSum = 0
    for i in range(len(romanList)):
        if i > 0 and romanDict[romanList[i]] > romanDict[romanList[i - 1]]:
            romanSum = romanSum + romanDict[romanList[i]] - 2 * romanDict[romanList[i - 1]]
        else:
            romanSum = romanSum + romanDict[romanList[i]]
    return romanSum
def high_and_low(numbers):
    numbers = str(numbers).split(" ")
    print(numbers)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    numbers.sort()
    print(numbers)
    returnArr = []
    returnArr.append(numbers[-1])
    returnArr.append(numbers[0])
    print(returnArr)
    return str(returnArr[0])+" "+str(returnArr[1])
def take(arr,n):
    returnArr = []
    if n > len(arr):
        return arr
    if arr == []:
        return []
    for i in range(0,n):
        returnArr.append(arr[i])
    return returnArr
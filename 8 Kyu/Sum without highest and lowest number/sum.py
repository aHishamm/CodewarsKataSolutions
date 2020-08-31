def sum_array(arr):
    if arr == None or arr == [] or len(arr) < 3: 
        return 0
    arr.sort()
    arr.pop()
    arr.pop(0)
    return sum(arr)
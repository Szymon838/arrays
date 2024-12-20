def second_largest(arr):
    arr_copy = arr[:]
    for i in range(len(arr_copy)):
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[i] > arr_copy[j]:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
    
    return arr_copy[-2]

def difference_largest_smallest(arr):
    arr_copy = arr[:]
    for i in range(len(arr_copy)):
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[i] > arr_copy[j]:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
    
    return arr_copy[-1] - arr_copy[0]

def median(arr):
    arr_copy = arr[:]
    for i in range(len(arr_copy)):
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[i] > arr_copy[j]:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
     
    n = len(arr_copy)
    if n % 2 == 1:
        return arr_copy[n // 2]
    else:
        mid = n // 2
        return (arr_copy[mid - 1] + arr_copy[mid]) / 2

def min_max(arr):
    arr_copy = arr[:]
    for i in range(len(arr_copy)):
        for j in range(i + 1, len(arr_copy)):
            if arr_copy[i] > arr_copy[j]:
                arr_copy[i], arr_copy[j] = arr_copy[j], arr_copy[i]
    
    return [arr_copy[0], arr_copy[-1]]

def array_to_string(arr):
    return "-".join(str(x) for x in arr)
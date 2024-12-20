def is_subset(arr1, arr2):
    for element in arr1:
        if element not in arr2:
            return False  
    return True  

arr1 = [2, 4, 5]
arr2 = [5, 4, 2, 6, 7]

result = is_subset(arr1, arr2)

if result:
    print(f"The first array {arr1} is a subset of the second array {arr2}.")
else:
    print(f"The first array {arr1} is not a subset of the second array {arr2}.")
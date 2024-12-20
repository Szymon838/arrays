def bubblesort(array):
    n = len(array)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

array1 = [64, 34, 25, 12, 22, 11, 90]
array2 = [5, 2, 9, 1, 5, 6]
array3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print("Original array1:", array1)
sorted_array1 = bubblesort(array1)
print("Sorted array1:", sorted_array1)

print("\nOriginal array2:", array2)
sorted_array2 = bubblesort(array2)
print("Sorted array2:", sorted_array2)

print("\nOriginal array3:", array3)
sorted_array3 = bubblesort(array3)
print("Sorted array3:", sorted_array3)
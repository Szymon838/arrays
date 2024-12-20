import random

arr1 = [3, 7, 1, 0, 4]
print("arr1:", arr1)

arr2 = [[2, 3], [7, 1], [0, 4]]
print("arr2:", arr2)

arr3 = [7 for i in range(5)]
print("arr3:", arr3)

arr4 = [i for i in range(1, 10)]
print("arr4:", arr4)

arr5 = [i * 2 for i in range(1, 10)]
print("arr5:", arr5)

arr6 = [random.randint(1, 20) for i in range(10)]
print("arr6:", arr6)

arr7 = [[] for i in range(5)]
print("arr7:", arr7)

arr8 = [[1 for i in range(2)] for j in range(4)]
print("arr8:", arr8)

arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]
print("arr9:", arr9)

arr = [4, 0, 3]
print("Array with values 4, 0, 3:", arr)

arr_zeros = [0] * 15
print("15-element array filled with zeros:", arr_zeros)

arr_range = [random.randint(1, 30) for _ in range(10)]
print("Array with integer values in the range of <1, 30>:", arr_range)

arr_binary = [random.choice([0, 1]) for _ in range(20)]
print("20-element array filled with 0 or 1 randomly:", arr_binary)

arr_false = [[False for _ in range(2)] for _ in range(5)]
print("2D array with False:", arr_false)
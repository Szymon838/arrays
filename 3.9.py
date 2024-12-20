def compare(array1, array2):
    if len(array1) == len(array2):  
        for i in range(len(array1)):  
            if array1[i] != array2[i]: 
                return False 
        return True  
    else:
        return False  

array1 = ["water", "book", "sky"]
array2 = ["water", "book", "sky"]

array3 = [True, False]
array4 = [True, False, True]

array5 = [5, 3, 1]
array6 = [5, 3, 1]

array7 = [3, 2, 1]
array8 = [3, 2]

def print_comparison_result(array1, array2):
    print(f"Array1: {' '.join(map(str, array1))}")
    print(f"Array2: {' '.join(map(str, array2))}")
    if compare(array1, array2):
        print("Comparison: arrays are the same\n")
    else:
        print("Comparison: arrays are not the same\n")

print_comparison_result(array1, array2) 
print_comparison_result(array3, array4)  
print_comparison_result(array5, array6)  
print_comparison_result(array7, array8)  
def flatten_2d_array(arr_2d):
    arr_1d = []
    
    for row in arr_2d:
        arr_1d.extend(row)
    
    return arr_1d

def print_1d_array(arr_1d):
    print("1D Array:", " ".join(map(str, arr_1d)))

def main():
    array_1 = [
        [2, 3],
        [1, 5]
    ]
    
    array_2 = [
        [5, 0, 3, 7, 5],
        [9, 0, 9, 1, 2]
    ]
    
    array_3 = [
        [2, 1],
        [3, 5],
        [7, 4],
        [2, 6]
    ]
    
    print("Array 1:")
    flattened_array_1 = flatten_2d_array(array_1)
    print_1d_array(flattened_array_1)
    
    print("\nArray 2:")
    flattened_array_2 = flatten_2d_array(array_2)
    print_1d_array(flattened_array_2)
    
    print("\nArray 3:")
    flattened_array_3 = flatten_2d_array(array_3)
    print_1d_array(flattened_array_3)

main()
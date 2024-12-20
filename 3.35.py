def transpose_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 0]
    ]

    matrix3 = [
        [5, 6, 7, 8]
    ]

    print("Original Matrix 1:")
    print_matrix(matrix1)
    print("\nTransposed Matrix 1:")
    print_matrix(transpose_matrix(matrix1))
    print()  

    print("Original Matrix 2:")
    print_matrix(matrix2)
    print("\nTransposed Matrix 2:")
    print_matrix(transpose_matrix(matrix2))
    print()  #

    print("Original Matrix 3:")
    print_matrix(matrix3)
    print("\nTransposed Matrix 3:")
    print_matrix(transpose_matrix(matrix3))

main()
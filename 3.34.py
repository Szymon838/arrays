def identity_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        matrix[i][i] = 1
    
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    print("Identity Matrix of size 3:")
    matrix_3 = identity_matrix(3)
    print_matrix(matrix_3)
    print()  
    
    print("Identity Matrix of size 5:")
    matrix_5 = identity_matrix(5)
    print_matrix(matrix_5)
    print()  
    
    print("Identity Matrix of size 8:")
    matrix_8 = identity_matrix(8)
    print_matrix(matrix_8)

main()
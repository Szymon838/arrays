array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

smallest_value = array[0][0]
largest_value = array[0][0]
smallest_position = (0, 0)
largest_position = (0, 0)

for i in range(len(array)):  
    for j in range(len(array[i])): 
        current_value = array[i][j]
        
        if current_value < smallest_value:
            smallest_value = current_value
            smallest_position = (i, j)
        
        if current_value > largest_value:
            largest_value = current_value
            largest_position = (i, j)

print(f"Smallest value: {smallest_value} at row {smallest_position[0]}, column {smallest_position[1]}")
print(f"Largest value: {largest_value} at row {largest_position[0]}, column {largest_position[1]}")
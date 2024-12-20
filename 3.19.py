def count_greater_than(arr, value):
    count = 0
    for num in arr:
        if num > value:
            count += 1
    return count

numbers = [1.2, 4.5, 7.3, 2.8, 5.1, 8.0, 3.6]

value = float(input("Enter a value to compare with: "))

count = count_greater_than(numbers, value)
print(f"Number of elements greater than {value}: {count}")
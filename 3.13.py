def occurs(number, array):
    return number in array

arr = [15, 38, 7, 23, 14]

number = int(input("Enter a number: "))

is_present = occurs(number, arr)

print("Array:", " ".join(map(str, arr)))
if is_present:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} does not appear in the array")
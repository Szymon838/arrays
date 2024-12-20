from collections import Counter

arr = [2, 3, 2, 5, 8, 1, 9, 8]

element_counts = Counter(arr)

unique_elements = [key for key, value in element_counts.items() if value == 1]

print("Array:", " ".join(map(str, arr)))
print("Unique elements:", " ".join(map(str, unique_elements)))
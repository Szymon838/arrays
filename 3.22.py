import random

def rand_elem(array):
    return random.choice(array)

arr = [10, 20, 30, 40, 50, 60, 70]

print("Randomly selected elements:")
for _ in range(5):  
    print(rand_elem(arr))
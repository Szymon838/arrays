names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

longest_name = ""

for name in names:
    if len(name) > len(longest_name):
        longest_name = name

print("Names:", " ".join(names))
print("Longest name:", longest_name)
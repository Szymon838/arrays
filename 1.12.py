categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_category_index = expenses.index(max_expense)
max_category = categories[max_category_index]

print(f"The most expensive category is: {max_category} with an expense of ${max_expense}")
monthly_expenses = [
   [200, 50, 100], 
   [180, 60, 110],  
   [220, 55, 105],  
   [210, 65, 95]    
]

total_food = 0
total_transport = 0
total_utilities = 0

for week in monthly_expenses:
    total_food += week[0]  
    total_transport += week[1]  
    total_utilities += week[2]  

week_totals = [sum(week) for week in monthly_expenses]

total_expenses = total_food + total_transport + total_utilities

print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_food)
print('Transport:', total_transport)
print('Utilities:', total_utilities)
print('Week 1:', week_totals[0])
print('Week 2:', week_totals[1])
print('Week 3:', week_totals[2])
print('Week 4:', week_totals[3])
print('---------------')
print('TOTAL:', total_expenses)
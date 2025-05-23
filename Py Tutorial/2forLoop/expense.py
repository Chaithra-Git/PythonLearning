expenses = [1200, 1300, 1400, 1500]

total_expense = 0
#for i in range(len(expenses)):
for i, monthly_expense in enumerate(expenses):
   # monthly_expense = expenses[i]
    total_expense += expenses[i]
    print(f"Month[{i+1}]: {monthly_expense}")

print(total_expense)
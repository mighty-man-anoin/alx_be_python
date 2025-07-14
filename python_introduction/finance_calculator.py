income = input('Enter your monthly income: ')
expenses = input('Enter your total monthly expenses: ')

savings = int(income) - int(expenses)

# projected_savings = (savings * 1.05) * 12
projected_savings = savings * 12 + (savings * 12 * 0.05)

print(f'Your monthly savings are ${savings}.')
print(f'Projected savings after one year, with interest, is: ${projected_savings}.')

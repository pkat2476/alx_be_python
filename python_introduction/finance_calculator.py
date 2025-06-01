>>> monthly_income = float(input("Enter your monthly income:"))
Enter your monthly income: 5000
>>> monthly_expenses = float(input("Enter your monthly expenses:"))
Enter your monthly expenses: 4000
>>> monthly_savings = monthly_income - monthly_expenses
>>> annual_savings_projection = (monthly_savings *12) + (monthly_savings * 12 * 0.05)
>>> print(f"Your monthly savings are ${int(monthly_savings)}.")
Your monthly savings are $1000.
>>> print(f"Projected savings after one year, with interest, is: ${int(annual_savings_projection)}")
Projected savings after one year, with interest, is: $12600.
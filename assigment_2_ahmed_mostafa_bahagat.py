team_members=int(input("Enter the number of team members: "))
month_number=float(input("Enter the month number the project will take: "))
monthly_salary=float(input("Enter the monthly salary : "))
total_cost=float(input("Enter the total cost of the project: "))
salary=team_members*monthly_salary*month_number
subtotal=salary+total_cost
vat=0.14*subtotal
total=subtotal+vat
print(f"the salary is: {salary:.2f}")
print(f"the subtotal is: {subtotal:.2f}")
print(f"the VAT is: {vat:.2f}")
print(f"the total is: {total:.2f}")
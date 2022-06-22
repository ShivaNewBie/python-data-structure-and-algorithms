annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input('Enter the cost of your dream home:'))
semi_annual_raise = float(input('Enter semi annual percentage'))


portion_down_payment = 0.25 * total_cost
current_savings = 0 
annual_return = (current_savings * 0.04 / 12)
monthly_salary = annual_salary / 12
no_of_months = 0
while current_savings < portion_down_payment:
    if no_of_months % 6 == 0 and no_of_months != 0: 
        annual_salary += annual_salary * semi_annual_raise
    
    current_savings += (current_savings * 0.04 / 12) + portion_saved * annual_salary / 12 

    no_of_months += 1

print(no_of_months)

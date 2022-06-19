#Part A: House Hunting
#You have graduated from MIT and now have a great job! You move to the San Francisco Bay Area anddecide that you want to start saving to buy a house.  As housing prices are very high in the Bay Area,you realize you are going to have to save for several years before you can afford to make the downpayment on a house. In Part A, we are going to determine how long it will take you to save enoughmoney to make the down payment given the following assumptions:
#1.Call the cost of your dream home ​total_cost​.2.Call the portion of the cost needed for a down payment ​portion_down_payment​. Forsimplicity, assume that portion_down_payment = 0.25 (25%).3.Call the amount that you have saved thus far ​current_savings​. You start with a currentsavings of $0. 4.Assume that you invest your current savings wisely, with an annual return of ​r ​(in other words,at the end of each month, you receive an additional ​current_savings*r/12​ funds to put intoyour savings – the 12 is because ​r​ is an annual rate). Assume that your investments earn a return of r = 0.04 (4%).5.Assume your annual salary is ​annual_salary​.6.Assume you are going to dedicate a certain amount of your salary each month to saving for the down payment. Call that ​portion_saved​. This variable should be in decimal form (i.e. 0.1for 10%). 7.At the end of each month, your savings will be increased by the return on your investment,plus a percentage of your ​monthly salary ​(annual salary / 12).Write a program to calculate how many months it will take you to save up enough money for a downpayment. You will want your main variables to be floats, so you should cast user inputs to floats

#Get the total cost and get the fixed downpayment 0.25 (25%)

#at end of each month you receive to your current savings this: test = 0 * 0.04/12


#we get annual salary
#we get a portion of our monthly salary for a percentage. say 10% or 0.10
#the portion saved 

#expected output: number of months

annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input('Enter the cost of your dream home:'))



portion_down_payment = 0.25 * total_cost
current_savings = 0 
annual_return = (current_savings * 0.04 / 12)
monthly_salary = annual_salary / 12
monthly_portion_saved = portion_saved * monthly_salary 
no_of_months = 0
while current_savings < portion_down_payment: 
    no_of_months += 1
    current_savings += (current_savings * 0.04 / 12) + monthly_portion_saved
print(no_of_months)


# A company has determined that its annual profit is typically 23 percent of its total sales
# Write a program that asks the users to enter the projected amount of total sales, and then
# displays the profit that will be made from that amount

# Enter the projected amount of sales
sales = float(input('Please enter the total amount that you expect to sell: '))
profit_percentage = 0.23

# Calculate the total profit earned
profit = sales * profit_percentage

# Return the results to the user
print('The total profit that you can expect to earn after you sell', 
	format(sales, ',.2f'), 
	'in merchandise, is', 
	format(profit, ',.2f' ))

amount = float( input("enter amount: "))

def number_of_quarters(change):
	no_quarters = change // 25
	return no_quarters, change - (no_quarters * 25)

def number_of_dimes(change):
	no_dimes = change // 10
	return no_dimes, change - (no_dimes * 10)

def number_of_nickels(change):
	no_nickels = change // 5
	return no_nickels, change - (no_nickels * 5)

def number_of_pennys(change):
	no_penny = change
	return no_penny, change - no_penny

while amount > 0:
	quarters, amount = number_of_quarters(amount)
	dimes, amount = number_of_dimes(amount)
	nickels, amount = number_of_nickels(amount)
	pennies, amount = number_of_pennys(amount)

print("You have {} quarters, {} dimes, {} nickels, and {} pennies.".format(quarters,dimes, nickels, pennies))

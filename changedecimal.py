from decimal import *

benjamin = Decimal('100.00')
grant = Decimal('50.00')
lincoln = Decimal('5.00')
jefferson = Decimal('2.00')
george = Decimal('1.00')
aquarter = Decimal('0.25')
adime = Decimal('0.10')
anickel = Decimal('0.05')
apenny = Decimal('0.01')

amount = Decimal(input("enter amount in dollars: "))

print("This is the amount you entered. ", amount)


def number_of_100notes(change):
	:no_benjamins = Decimal(change // benjamin)
	return 


def number_of_quarters(change):
no_quarters = Decimal(change // aquarter)
    return no_quarters, change - (no_quarters * aquarter)


def number_of_dimes(change):
    no_dimes = Decimal(change // adime)
    return no_dimes, change - (no_dimes * adime)


def number_of_nickels(change):
    no_nickels = Decimal(change // anickel)
    return no_nickels, change - (no_nickels * anickel)


def number_of_pennys(change):
    no_penny = Decimal(change // apenny)
    return no_penny, change - (no_penny * apenny)


while Decimal(amount) > 0:
    print(amount)
    quarters, amount = number_of_quarters(amount)
    dimes, amount = number_of_dimes(amount)
    nickels, amount = number_of_nickels(amount)
    pennies, amount = number_of_pennys(amount)

print("You have {} quarters, {} dimes, {} nickels, and {} pennies.".format(quarters, dimes, nickels, pennies))

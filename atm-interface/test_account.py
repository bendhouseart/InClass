import account_test as a

x1 = a.Account(100, 'Anthony')

x1.get_funds()

if x1.check_withdrawal(50) == True:
	x1.withdraw(50)

x1.calc_interest()

x1.deposit(1000000)

x1.get_funds()

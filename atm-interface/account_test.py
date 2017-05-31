class Account:
	def __init__(self,balance, name):
		self.balance = balance
		self.name = name

	def get_funds(self):
		print('The balance for {}\'s account is ${}'.format(self.name, self.balance))

	def deposit(self, amount):
		self.balance += amount
		print('With a deposit of ${} your current balance is now ${}.'.format(amount, self.balance))

	def check_withdrawal(self, amount):
		return  amount <= self.balance


	def withdraw(self, amount):
		if self.check_withdrawal(amount) == True:
			self.balance -= amount
			print('After a withdrawal of ${} your current balance is now ${}'.format(amount, self.balance))
		else:
			print('Insufficient Funds.')
		

	def calc_interest(self, interest = 0.01):
		print('Your current balance of ${} just incurred intrest and is now ${}.'.format(self.balance, (self.balance*(interest + 1))))
		self.balance = self.balance*(interest + 1)	

# camel case in python is first letter of everyword is capitalize


'''
class Person: #this is a class at its most elemental
	pass
'''

# classes inherit from  a parent object instructor, more on that latter.
# the take away from that is that we don't need to supply an argument 
# in a class constructor.

''' Now let's give class Person som pizzzazz '''

class Person:
	def __init__(self,name):
		self.name = name

	def print_name(self):
		print(self.name)

	def __str__(self):
		return 'Person class of {} '.format(self.name)
	def __repr__(self):
		return self.__str__()


# note:  a method is a function that is inside of a class.
# **every method inside of a class needs to take self as a first argument.

chris = Person('Chris')

chris.print_name()

# We can sign a unique attribute to an instance of a class.
chris.phone = '503-277-9710'

print(chris.phone)

print(chris)

print([chris])


class BankAccount:
	def __init__(self, balance, acc_name):
		self.balance = balance
		self.acc_name = acc_name

	def withdrawl(self, amount):
		if self.balance - amount > 0:
			self.balance -= amount
		print('Thank you {}. Your remaining balance is {} . '.format(self.acc_name, self.balance))
		print('Sorry, you have no money.')
	
	def deposit(self, amount):
		self.balance += amount
		print('Thank you {}. Your balance is {}.'.format(self.acc_name, self.balance))

	def __str__(self):
		return 'Hello {}, your balance is {}'.format(self.acc_name, self.balance)


class BankAccountSpecial(BankAccount):
	def __init__(self, balance, acc_name):
		super().__init__(balance, acc_name)
	
	def withdrawl(self, amount):
		if self.balance - amount >= 100:
			self.balance -= amount
		print('Thank you {}. Your remaining balance is {} . '.format(self.acc_name, self.balance))
		if 100 > self.balance - amount >= 0:
			print('You can\'t withdraw {} you dirty peasant. Show some god damn discipline. Boot straps!'.format(amount)
acc1 = BankAccount(100, 'Katie')

print(acc1)

acc1.deposit(500)

acc1.withdrawl(1000)

acc2 = BankAccountSpecial(200, 'Chris')
acc2.withdrawl(101)




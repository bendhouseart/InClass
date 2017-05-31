class Car(self):
	def __init__(self, model):
		self.model = model

	def number_of_wheels(self):
		self.wheels = 4

	def color(self, color):
		self.color = color

	def number_of_doors(self, no_doors):
		self.doors = no_doors

	def __str__(self):
		return '{}, Number of wheels: {}, Color: {}, Number of doors: '.format(self.model, self.wheels, self.doors)

	def honk(self):
		print('honk')
		 

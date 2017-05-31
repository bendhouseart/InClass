class Car:
	def __init__(self, model, wheels, color, doors):
		self.model = model
		self.wheels = wheels
		self.color = color
		self.doors = doors
		

	def number_of_wheels(self):
		self.wheels = 4

	def color(self, color):
		self.color = color

	def number_of_doors(self, doors):
		self.doors = doors

	def __str__(self):
		return '{}, Number of wheels: {}, Color: {}, Number of doors: {} '.format(self.model, self.wheels, self.color,  self.doors)

	def honk(self):
		print('honk')
		 

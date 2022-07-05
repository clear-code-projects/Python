class Monster:

	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	def __len__(self):
		return self.health

	def __abs__(self):
		return self.energy

	def __call__(self):
		print('The monster was called')

	def __add__(self,other):
		return self.health + other

	def __str__(self):
		return f'A monster with health {self.health} and energy {self.energy}'

	# methods 
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		monster.energy -= 20
		print(self.energy)

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

monster1 = Monster(10,20)
print(str(monster1))
print(monster1)


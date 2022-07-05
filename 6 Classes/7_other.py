class Monster:
	'''A monster that has some attributes'''
	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

		# private attributes 
		self._id = 5

	# methods 
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		self.energy -= 20
		
	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

monster = Monster(20,10)

# hasattr and setattr
# if hasattr(monster,'health'):
# 	print(f'the monster has {monster.health} health')

setattr(monster,'weapon', 'Sword')
# monster.weapon = 'Sword'
# print(monster.weapon)

# new_attributes = (['weapon','Axe'],['armor','Shield'],['potion','mana'])
# for attr,value in new_attributes:
# 	setattr(monster,attr,value)
# print(vars(monster))

# doc
# print(monster.__doc__)
help(str)
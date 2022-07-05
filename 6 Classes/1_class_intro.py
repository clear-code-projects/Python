# health = 0
# def scope_test():
# 	health += 1
# scope_test()
# print(health)

class Monster:

	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	# methods 
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		monster.energy -= 20
		print(self.energy)

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

	def get_damage(self,amount):
		self.health -= amount

class Hero:
	def __init__(self,health,damage,monster):
		self.health = health
		self.damage = damage
		self.monster = monster

	def attack(self):
		self.monster.get_damage(self.damage)

monster = Monster(health = 50, energy = 40)
# monster.weapon = 'axe'
# print(vars(monster))

print(monster.health)
hero = Hero(health = 100, damage = 20, monster = monster)
hero.attack()
print(monster.health)
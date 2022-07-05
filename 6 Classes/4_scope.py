# scope problem
def update_health(amount):
	monster.health += amount

# health = 10
# print(health)
# update_health(20)
# print(health)

class Monster:
	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	def update_energy(self,amount):
		self.energy += amount

	# 2. the monster class should have a method that lowers the health -> get_damage(amount)
	def get_damage(self,amount):
		self.health -= amount

# exercise 
# 1. create a hero class with 2 parameters: damage, monster
class Hero:
	def __init__(self,damage,monster):
		self.damage = damage
		self.monster = monster

# 3. the hero class should have an attack method that calls the get_damage method from the monster
# the amount of damage is hero.damage
	def attack(self):
		self.monster.get_damage(self.damage)

monster = Monster(health = 100, energy = 50)

hero = Hero(damage = 15, monster = monster)
print(monster.health)
hero.attack()
print(monster.health)
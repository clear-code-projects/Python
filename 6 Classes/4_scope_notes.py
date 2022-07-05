health = 10
def update_health(amount):
	health += amount
update_health(20)
print(health)

class Monster:

	def __init__(self,health,energy):
		self.health = health
		self.energy = energy

	# methods 
	def attack(self,amount):
		print('The monster has attacked!')
		print(f'{amount} damage was dealt')
		monster.energy -= 20

	def move(self,speed):
		print('The monster has moved')
		print(f'It has a speed of {speed}')

	def get_damage(self,amount):
		self.health -= amount

# exercise 
class Hero:
	def __init__(self,damage,monster):
		self.damage = damage
		self.monster = monster

	def attack(self):
		self.monster.get_damage(self.damage)

monster = Monster(40,10)
# monster.weapon = 'Axes'
# print(monster.weapon)
def test():
	monster.health += 10
test()
print(monster.health)

hero = Hero(10,monster)
# print(monster.health)
# hero.attack()
# print(monster.health)

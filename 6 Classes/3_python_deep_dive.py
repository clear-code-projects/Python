# def add(a,b):
# 	return a + b

# class Test:
# 	def __init__(self,add_function):
# 		self.add_function = add_function

# test = Test(add_function = add)
# print(test.add_function(1,2))

# create a Monster class with a parameter called func, store this func as parameter 
class Monster:
	def __init__(self,func):
		self.func = func

# create another class, called Attacks, that has 4 methods: 
# bite, strike, slash, kick (each method just prints some text)

class Attacks:
	def bite(self):
		print('bite')

	def strike(self):
		print('strike')

	def slash(self):
		print('slash')

	def kick(self):
		print('kick')

# create a monster object and give it one of the attack methods from the attack class  
attacks = Attacks()
monster = Monster(func = attacks.bite)
monster.func()
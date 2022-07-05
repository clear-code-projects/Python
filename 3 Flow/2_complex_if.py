# combining conditions
# if True and True and False or True:
# 	print('True')

# Exercise 
# money_available = 100
# hungry = False
# bored = True

# check if money_available > 80 and if hungry is true or if bored
# if money_available > 80 and hungry == True or bored == True:
# 	print('eat something fancy!')

# nested if statements
# x = '1'
# if x in ['a','b','1']:
# 	print('a is in the list')
	
# 	if x.isalpha():
# 		print('it is a letter')

# 	if True:
# 		print('something')
	

# exercise 
money_available = 100
hungry = True
bored = True
# create a nest if statement that runs of all 3 conditions are true (money > 80 for the first one)
if money_available > 80:
	print('I have enough money!')
	if hungry:
		print('and I am hungry!')
		if bored:
			print('Eat something fancy :)')
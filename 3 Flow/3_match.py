# mood = 'bored' 

# match mood:
# 	case 'hungry':
# 		print('get some food')
# 	case 'thirsty':
# 		print('get some water')
# 	case 'tired':
# 		print('get some sleep')
# 	case _:
# 		print('any other mood')

# exercise 
# create a variable with an integer between 1 and 5, call it grade 
# create a match case statement that writes 'very good' when the grade is 1
# and very bad when the grade is 5 (and all other cases in between)
# there should also be some default behaviour if you get an unexpected value

grade = 'something else'

match grade:
	case 1:
		print('very good!')
	case 2:
		print('good')
	case 3:
		print('okay')
	case 4:
		print('needs improvement')
	case 5:
		print('very bad')
	case _:
		print('Grade not recognized')
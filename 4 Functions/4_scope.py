# a = 10 

# def test_func_3(a):
# 	a += 2
# 	# print(a)
# 	return a

# a = test_func_3(a)
# print(a)
# def test_func():
# 	capacity = 2
# 	print(capacity)

# def test_func_2():
# 	capacity = 200
# 	print(capacity)

# test_func()
# test_func_2()

#exercise 
# create 2 global variables called 'multiplier' and has_calculated
# multiplier should have any integer and has_calculated should be set to the boolean False

# then create a function called multiply_calculator that takes one argument and calculates
# the multiplication of that number
# inside of the function multiply the parameter with the global variable multiplier 
# once the calculation is done set has_calculated to True
# store that new number a variable called result and return it 
# print the return value of the function (after it was called with the number)

multiplier = 5
has_calculated = False

def multipy_calculator(number):
	global has_calculated
	has_calculated = True
	result = number * multiplier
	return result

print(multipy_calculator(10))
print(has_calculated)
def test_function():
	print('hello')
	test = 1 + 2
	print(test)

def calculator(num1,num2):
	result = num1 + num2
	print(result)

def better_calculator(num1,num2,operation):
	if operation == 'plus':
		result = num1 + num2
		print(f'{num1} + {num2} = {result}')
	elif operation == 'minus':
		result = num1 - num2
		print(f'{num1} - {num2} = {result}')

# calculator(2,3)
# calculator(10,20)

# exercise 
better_calculator(1,2,'minus')
better_calculator(4134,100,'plus')
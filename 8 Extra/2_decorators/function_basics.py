def func():
	print('Function')

def wrapper(func):
	print('hello')
	func()
	print('goodbye')

def function_generator():
	def new_function():
		print('New function')
	return new_function

new_func = function_generator()
new_func()
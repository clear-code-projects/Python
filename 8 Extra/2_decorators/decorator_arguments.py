def decorator(func):
	def wrapper(*args,**kwargs):
		print('decoration begins')
		func(*args,**kwargs)
		print('decoration ends')
	return wrapper

@decorator
def func(func_parameter):
	print(func_parameter)
#func = decorator(func)

func('something')
def repetition_decorator(repetitions):
	def decorator(func):
		def wrapper():
			for r in range(repetitions):
				func()
		return wrapper
	return decorator

@repetition_decorator(4)
def func():
	print('Function')

#func = repetition_decorator(4)(func)
func()
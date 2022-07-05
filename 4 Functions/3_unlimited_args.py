# list unpacking
def print_all(first,*arguments,extra):
	print(first)
	print(arguments)
	print(extra)
	# print all arguments
	for argument in arguments:
		print(argument) 

# keyword unpacking
def print_more(**arguments):
	print(arguments)

def print_even_more(*args, **kwargs):
	print(args)
	print(kwargs)

# exercises 
# create a calculator function that prints the sum of an unlimited amount of numbers
def calculator(*args):
	result = sum(args)
	print(result)

sum()
abs()
len()

# print_all(1,2,3,4,5,'hello',1,3,213,321,3,123,123,extra = 12)
# print_more(arg1 = '1', arg2 = 'test', arg3 = [1,2,3])
# print_even_more(1,2,3,54,21,3412,31,'hello',True)
calculator(1,2,3,4,5,6)

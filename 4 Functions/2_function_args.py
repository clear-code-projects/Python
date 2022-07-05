def test_function(arg1 = 'Argument 1', arg2 = 'Argument 1', arg3 = 'Argument 3',arg4 = 'Argument 4'):
	print(arg1)
	print(arg2)
	print(arg3)
	print(arg4)

# exercise 
# create greeter function with 3 parameters: person, greet and weekday
# person and greet should have default arguments ('Person' for person and 'Hello' for greet)
# inside of the function use an f-string to print the greet and the person and also print the weekday
# when calling the function, use at least one positional argument and 1 keyword argument  
def greeter(person = 'Person', greet = 'Hello', weekday = 'Monday'):
	print(f'{person} {greet}')
	print(f'It is {weekday}')

# test_function()
greeter('Bob', 'Tuesday','Welcome')


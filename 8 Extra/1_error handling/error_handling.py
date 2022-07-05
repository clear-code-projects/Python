# anticipating errors / exceptions
# try:
# 	print('try')
# 	# print(a)
# 	print(1/0)
# except ZeroDivisionError:
# 	print('You cannot divide by 0')
# except NameError:
# 	print('Does not exist')
# else:
# 	print('The else statment')
# finally:
# 	print('finally...')

# raising exceptions 
# var_must_be_string = []
# if isinstance(var_must_be_string,str):
# 	print(var_must_be_string)
# else:
# 	raise TypeError('Must be a string')

# assert 
# a = 6
# assert a == 5

# exercise 
# create a list and
# try to raise an Index error 
# also add else and finally 

my_list = [1,2,3,4,5]
try:
	print(my_list[99])
except IndexError:
	print('That index does not exist')
else:
	print('That index exists')
finally:
	print('finished')
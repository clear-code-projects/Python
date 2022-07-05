# print(eval('"test".upper()'))
# exec('a = 10')

my_string = 'test'
# print(my_string.upper())
# print(my_string.title())
# print(my_string.lower())
# print(my_string.casefold())

for operation in ['upper', 'title', 'lower', 'casefold']:
	print(eval(f'my_string.{operation}()'))
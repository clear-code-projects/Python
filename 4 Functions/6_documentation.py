def test(a:int = 10, b:int = 0) -> int:
	'''A simple function that prints 2 parameters'''
	print(a)
	print(b)
	return a + b

test('string', 'test')
# print(test.__doc__)
# help(test)
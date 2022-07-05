def test_function(content):
	print(f'this is an imported function with the parameter: {content}')

class Test:
	def __init__(self):
		self.name = 'My App'
		self.value = 12

	def do_something(self):
		print('hello')

test_var = 'test'

# create a sum calculator function
# that takes unlimited arugments and returns the sum
# create it here and run it in the main file

def sum_calculator(*nums):
	return sum(nums)

if __name__ == '__main__':
	print(__name__)
# open and close it manually
# file = open('test.txt')
# print(list(file))
# file.close()

# open and close it automatically 
# with open('test.txt') as file:
# 	#print(file.read())
# 	for line in list(file):
# 		print(line)

# write some file
# with open('new_file.txt','w') as file:
# 	file.write('\nXXXXXXWrite some more textXXXXXX')

# exercise 
# create a new text file and draw a tree in it
with open('tree.txt','w') as tree_file:
	tree_string = '''
	  x
	 xxx
	xxxxx
	  x
	  x
	  x 
	'''
	tree_file.write(tree_string)

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
with open('test.txt','a') as file:
	file.write('XXXXXXWrite some more textXXXXXX')
# basic_list = [1,2,3]
# basic_tuple = (1,2,3)
# basic_set = {1,2,3}
# basic_dict = {1:'one', 2: 'two', 3: 'three'}
# basic_string = 'One two three'
# basic_num = 3

# for x in range(10,20,2):
# 	print(x)

# exercise 
practice_list = [[10,40,20,50], [2,42,10], [101,12,4]]
# use a for loop to only print the numbers below 50
# skip values below 10
# end the entire loop if a value is above 100
for nested_list in practice_list:
	# print(nested_list)
	for value in nested_list:
		if value > 100:
			break
		if value < 50:
			if value < 10:
				continue
			
			print(value)
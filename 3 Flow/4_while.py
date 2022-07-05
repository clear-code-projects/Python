# x = 0
# while x < 10:
# 	x += 1

# 	if x == 5:
# 		continue
	
# 	print(x)

# exercise 
# use a while loop to create a list with only even values from 0 to 100
# Do not add the value 58! 

my_list = []
counter = 0

while counter <= 100:
	if counter % 2 == 0:
		if counter != 58:
			my_list.append(counter)
	counter += 1

print(my_list)
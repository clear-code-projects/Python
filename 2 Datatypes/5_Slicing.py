test_list = [1,2,3,4,5,6,7,8,9,10]

negative_slicing = test_list[-1:4:-1]

default_slicing = test_list[::]

# exercise: 
# start from 8 and go to 2, pick every second element
solution = test_list[7:0:-2]
# print(solution)

# tuple slicing
test_tuple = (1,2,3,4,5,6,7,8,9,10)
print(test_tuple[0:5:3])
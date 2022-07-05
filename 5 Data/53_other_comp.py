# set_comp = {num for num in range(100)}
# dict_comp = {num: num ** 2 for num in range(100)}
# tuple_comp = tuple(num for num in range(100))
# print(tuple_comp)

# exercise 
# create a dictionary with the keys 'A', 'B', 'C', 'D' and 'E'
# each key should have a list as value with the values [1,2,3,4,5]

exercise_comp = {letter:[1,2,3,4,5] for letter in 'ABCDE'}
print(exercise_comp)
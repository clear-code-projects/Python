# my_set = {1,2,3,4,4} # dublicate values will be exterminated 

# use methods 
# my_set.add(5)
# my_set.remove(2)
# print(len(my_set))
# print(my_set)

# indexing and slicing does NOT work
# print(my_set[0])
# print(my_set.pop())
# exercise 
# use type conversion to get one item from the set by index
# print(list(my_set)[0])

# comparison operators 
set1 = {1,2,3,4,4}
set2 = {4,5,6,7}

# print(set1.union(set2))
# print(set1 | set2)
# print(set1.intersection(set2))
# print(set1 & set2)
# print(set1.difference(set2))
# print(set1 - set2)

# exercise 
# check if the list below has dublicate values
test_list = [43,25,324,234,5,2,32423,542,534,324,23,54,65,323,42,4,123,123,5,1,321,3124,123,123,124,1,31,23,145,3542,43,3,21,312]

print(len(test_list))
print(len(set(test_list)))
print(len(test_list) == len(set(test_list)))
test_string = 'this is a test'
test_list = [1,2,3,4]

# turning a string into a list / tuple 
# print(test_string.split())
# print(list(test_string))
# print(tuple(test_string))

# turn a list / tuple into a string 
# print(' '.join(['one','two','three','four']))
# print(' '.join(test_list))
# print(str(test_list))

# indexing on strings 
# print(test_string[0:5])

# exercise 
# remove all the stuff to only get 1 2 3 4 
exercise = str(test_list).strip('[').strip(']').replace(',','').replace(' ','')
print(exercise)
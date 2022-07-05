# a = lambda x: x + 1
# simple_calc = lambda a,b: a + b

# some functions want other functions as argument 
# sort([1,5,2,3,4],func)

# graphical user interfaces 

# exercise 
# create a lambda function that accepts 1 integer argument
# if the integer is > 5 return hello
# otherwise return bye 

x = lambda x: 'hello' if x > 5 else 'bye'
print(x(10))
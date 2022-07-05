
# quotes for strings
# test_var = 'Test 1'
# test_var2 = "Test 2"
# print(test_var)
# print(test_var2)

# qotes inside of strings 
# test_var3 = "He said 'This was great'"
# test_var4 = '\"\'' # simple escape character
# print(test_var4)

# escape characters 
# test_var5 = 'Line 1: some text \nLine 2: some more text'
# print(test_var5)

# multiple lines 
# test_var6 = '''   x
#   xxx
#  xxxxx
#    x
#    x'''
# print(test_var6)

# math and strings 
# test_var7 = 'hello' + " " +  'World'
# test_var8 = 'copy' * 10
# print(test_var8)

# how to get values into strings 
# name = 'Bob'
# age = 40
# greeting_string = 'Hello {one}, you are {two} years old'.format(one = name, two = age)
# greeting_string_better = f'Hello {name}, you are {age + 10} years old'
# print(greeting_string_better)

# exercise 
# create an f-string that says: Hello, my name is X and my hobby is Y
# X and Y should be separate variables 
# the second half of the sentence should also be on a separate line
X = 'Lisa'
Y = 'programming'
exercise_string = f'Hello, my name is {X} \nand my hobby is {Y}'
exercise_string2 = f'''Hello, my name is {X}
and my hobby is {Y}'''
print(exercise_string2)
# my_list = []
# for num in range(0,100):
# 	my_list.append(num)

# my_list_comp = [(num,num,num) if num < 20 else 0 for num in range(0,100)]

# inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
# inventory_numbers = [43, 12, 95, 421, 23, 43]
# replenish_list = [(name,number) for name, number in zip(inventory_names, inventory_numbers) if number < 25]

# print(replenish_list)

# combine list comprehension
# combined_comp = [[(x,y) for x in range(5)] for y in range(10)]
# for row in combined_comp:
# 	print(row)

# exercise 
# create the fields for a chess board 
# abcdefgh
# 12345678

chess_board = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
for row in chess_board:
	print(row)
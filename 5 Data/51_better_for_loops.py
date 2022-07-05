inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

# for name, number in zip(inventory_names,inventory_numbers):
# 	print(f'{name} current inventory: {number}')

# enumerate function - get the current index 
# for index, name in enumerate(inventory_names):
# 	print(f'{index}: {name}')
# 	if index == len(inventory_names) // 2:
# 		print('halfway done!')

# Exercise 
# combine zip and enumerate to get 'Screws [id: 0] - inventory: 43'
for index, inventory_tuple in enumerate(zip(inventory_names,inventory_numbers)):
	print(f'{inventory_tuple[0]} [id: {index}] - inventory: {inventory_tuple[1]}')

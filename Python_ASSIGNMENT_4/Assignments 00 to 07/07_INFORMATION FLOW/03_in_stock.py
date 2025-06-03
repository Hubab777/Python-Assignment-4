def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print("This fruit is in stock! Here is how many:")
		print(stock)


def num_in_stock(fruit):
	"""
	This function returns the number of fruit Zuni has in stock.
	"""
	if fruit == 'custard-apple':
		return 2
	if fruit == 'raspberry':
		return 4
	if fruit == 'peach':
		return 1000
	else:
		# this fruit is not in stock.
		return 0


if __name__ == '__main__':
    main()
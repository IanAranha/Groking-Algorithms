def binary_search (list, item):
	low = 0
	high = len(list)-1
	counter = 1

	while low <= high:
		mid = (low + high)/2
		guess = list[mid]

		if guess == item:
			print 'Correct'
			print 'It took', counter, 'cycles to guess.'
			return mid

		if guess > item:
			counter = counter+1
			print 'too high'
			high = mid - 1
		else:
			counter = counter+1
			print 'too low'
			low = mid + 1
	return None

my_list = [1,2,3,4,5,6,7,8,9,10]

binary_search(my_list, 5)
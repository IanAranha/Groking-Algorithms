#Assuming you have a pre-sorted array of numbers. You guess a number and then with minimum guesses, 
#the computer needs to guess the number

#I have added a few variations such as adding a counter to let the progammer know how many guesses it took.

#Since this is a binary search, the algoritm guts the array by half searching for the number each operation.
#Therefore, the efficieny of the method is O(log n)

#PseudoCode
#Establish low pointer and high pointers at opposite extremes of the array
#As long as low is not equal to high, find the midpoint index.
#if the mid-point index is the correct number, exit and return that index.

#else

#if the midpoint index value is larger than the number to be guessed, means the guess number must be smaller
	#move the high pointer to mid+1 and repeat searh
#else
	#the midpoint index value is smaller than the number to guessed, means the guess number myst be bigger
	#move the low pointer to the mid+1 and repeat search


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
my_list2 = [2,34,45,67,99,100,156,223,675,990,1004,1997]

binary_search(my_list, 5)
binary_search(my_list2, 990)
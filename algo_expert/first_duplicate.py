def firstDuplicateValue(array):
    # Write your code here.
	for num in array:
		val = abs(num)
		if array[val - 1] < 0:
			return val
		array[val - 1] *= -1

	return -1

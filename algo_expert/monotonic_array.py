def isMonotonic(array):
    if len(array) == 0 or len(array) == 1:
        return True
	i = 1
	while i < len(array) and array[i] == array[i-1]:
		i += 1

	if i == len(array):
	    return True

	diff = array[i-1] - array[i]

	if diff > 0:
		while i <= len(array) - 1:
			print(array[i])
			if array[i-1] < array[i]:
				return False
			i += 1

	if diff < 0:
		while i <= len(array) - 1:
			if array[i-1] > array[i]:
				return False
			i += 1
	return True

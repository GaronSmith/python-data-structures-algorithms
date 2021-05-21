def moveElementToEnd(array, toMove):
    # Write your code here.
	i, j = 0, len(array) - 1
	while i <= j:
		print(i, j, array)
		while array[j] == toMove and i < j:
			j -= 1
		while array[i] != toMove and i < j:
			i += 1

		array[j], array[i] = array[i], array[j]
		j -= 1
		i += 1

	return array

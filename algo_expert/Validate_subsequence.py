def isValidSubsequence(array, sequence):
    # Write your code here.
	i, j = len(array) - 1, len(sequence) - 1
	while i >= 0 and j >= 0:
		curr_arr, curr_seq = array[i], sequence[j]
		if curr_arr != curr_seq:
			i -= 1
		else:
			i -= 1
			j -= 1

	return j < 0

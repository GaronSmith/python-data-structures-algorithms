def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if not array:
        return 0
	max_sums = [0 for _ in array]
	max_sums[0] = array[0]
	for i in range(1, len(array)):
		max_sums[i] = max(max_sums[i-1], max_sums[i-2] + array[i])

	return max_sums[-1]

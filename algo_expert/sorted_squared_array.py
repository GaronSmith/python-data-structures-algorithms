def sortedSquaredArray(array):
	i, j = 0, len(array) - 1
	ans = [0 for _ in array]
	k = len(ans) - 1
	while k >= 0 and i <= j:
		left = abs(array[i])
		right = abs(array[j])
		if(left >= right):
			ans[k] = left**2
			i += 1
		else:
			ans[k] = right**2
			j -= 1

		k -= 1
	return ans

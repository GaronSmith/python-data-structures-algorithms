def arrayOfProducts(array):
    # Write your code here.
    arr_left = []
	total = 1
	for num in array[:-1]:
		total *= num
		arr_left.append(total)
	
	total = 1
	arr_right = []
	for num in reversed(array[1:]):
		total *= num
		arr_right.append(total)
	ans = []
	start = arr_right.pop()
	end = arr_left.pop()
	ans.append(start)
	for i,num in enumerate(reversed(arr_right)):
		 ans.append(num * arr_left[i])
	ans.append(end)
	return ans
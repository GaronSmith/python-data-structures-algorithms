def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i, j = len(matrix) - 1, 0


while i >= 0 and j < len(matrix[0]):
		curr = matrix[i][j]
		print(curr)
		if target > curr:
			j += 1
		elif target < curr:
			i -= 1
		elif target == curr:
			return [i, j]

	return [-1, -1]

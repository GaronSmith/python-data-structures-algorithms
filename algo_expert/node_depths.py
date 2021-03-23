def nodeDepths(root):
    # Write your code here.
	total = []
	calcSum(root, total, 0)
	return sum(total)


def calcSum(root, total, level):
	if root is None:
		return
	total.append(level)
	calcSum(root.left, total, level + 1)
	calcSum(root.right, total, level + 1)

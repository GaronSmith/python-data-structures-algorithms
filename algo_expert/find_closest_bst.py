def findClosestValueInBst(tree, target):
    # Write your code here.
	diff = float('inf')
	val = tree.value
	while tree:
		if tree.value > target and tree.left:
			if(abs(tree.left.value - target) < diff):
				diff = abs(tree.left.value - target)
				val = tree.left.value
			tree = tree.left
		elif tree.value < target and tree.right:
			if(abs(tree.right.value - target) < diff):
				diff = abs(tree.right.value - target)
				val = tree.right.value
			tree = tree.right
		else:
			return val

	return val

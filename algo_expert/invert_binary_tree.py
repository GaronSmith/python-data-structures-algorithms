def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
	swap(tree)
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)


def swap(tree):
	tree.left, tree.right = tree.right, tree.left 

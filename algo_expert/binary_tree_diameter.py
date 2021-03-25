# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
	if tree is None:
		return TreeInfo(0, 0)

	left_tree = getTreeInfo(tree.left)
	right_tree = getTreeInfo(tree.right)
	longest_path = left_tree.height + right_tree.height
	max_diameter = max(left_tree.diameter, right_tree.diameter)
	curr_diameter = max(longest_path, max_diameter)
	curr_height = 1 + max(left_tree.height, right_tree.height)
	return TreeInfo(curr_diameter, curr_height)


class TreeInfo:
	def __init__(self, diameter, height):
		self.diameter = diameter
		self.height = height

def minHeightBst(array):
	return recursive_min_height_bst(array, None, 0, len(array) - 1)


def recursive_min_height_bst(array, bst, start_idx, end_idx):
	if end_idx < start_idx:
		return

	mid_idx = (start_idx + end_idx) // 2
	new_node = BST(array[mid_idx])

	if bst is None:
		bst = new_node
	else:
		if array[mid_idx] < bst.value:
			bst.left = new_node
			bst = bst.left
		else:
			bst.right = new_node
			bst = bst.right

	recursive_min_height_bst(array, bst, start_idx, mid_idx - 1)
	recursive_min_height_bst(array, bst, mid_idx + 1, end_idx)
	return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

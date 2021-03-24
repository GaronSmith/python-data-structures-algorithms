def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	node = linkedList
	while node is not None:
		next_node = node.next
		while next_node is not None and next_node.value == node.value:
			next_node = next_node.next

		node.next = next_node
		node = node.next

	return linkedList

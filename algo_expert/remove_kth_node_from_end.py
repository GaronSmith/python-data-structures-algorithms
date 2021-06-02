def removeKthNodeFromEnd(head, k):
    # Write your code here.
	counter = 1
	first = head
	second = head
	while counter <= k:
		second = second.next
		counter += 1

	if second is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while second.next is not None:
		second = second.next
		first = first.next
	first.next = first.next.next

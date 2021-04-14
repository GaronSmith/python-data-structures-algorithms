class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        less = less_head = ListNode()
        more = more_head = ListNode()

        while head:
            if head.val >= x:
                more.next = head
                more = more.next
            elif head.val < x:
                less.next = head
                less = less.next
            head = head.next

        more.next = None
        less.next = more_head.next

        return less_head.next

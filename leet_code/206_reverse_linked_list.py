class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # stack = []
        # while head:
        #     stack.append(head.val)
        #     head = head.next
        # ans_head = prev = ListNode()
        # while stack:
        #     prev.next = ListNode(stack.pop())
        #     prev = prev.next
        # return ans_head.next
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

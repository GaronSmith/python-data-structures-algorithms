class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        l, r = 0, len(arr) - 1
        while l <= r:
            left, right = arr[l], arr[r]
            if(left is not right):
                return False
            l += 1
            r -= 1

        return True

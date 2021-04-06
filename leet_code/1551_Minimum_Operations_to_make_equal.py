
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return int((n/2)**2)
        else:
            return int((n//2)*(n//2+1))

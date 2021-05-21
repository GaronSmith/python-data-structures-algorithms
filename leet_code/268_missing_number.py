class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        dif = int(((length * (length+1)) / 2) - sum(nums))
        return dif if dif else 0

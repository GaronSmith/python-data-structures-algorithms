from collections import defaultdict
class Solution:
    def twoSum(self, nums, target): 
        ans = defaultdict(int)
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ans:
                return [ans[diff], i]
            else:
                ans[num] = i

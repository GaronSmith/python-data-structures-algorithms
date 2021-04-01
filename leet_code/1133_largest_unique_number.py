from collections import defaultdict


class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        ref = defaultdict(int)
        for num in A:
            ref[num] += 1

        max_num = -1
        for num in ref:
            if(ref[num] == 1 and num > max_num):
                max_num = num

        return max_num

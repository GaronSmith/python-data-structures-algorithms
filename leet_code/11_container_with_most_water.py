class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxi = float('-inf')
        while l < r:
            print('l', l, 'r', r, maxi)
            if(height[l] > height[r]):
                val = height[r] * (r-l)
                if (val > maxi):
                    maxi = val
                r -= 1
            else:
                val = height[l] * (r-l)
                if (val > maxi):
                    maxi = val
                l += 1
        return maxi

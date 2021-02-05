class Solution:
    def maxProfit(self, prices):
        mini = prices[0]
        maxi = float('-inf')
        total = 0
        for num in prices:
            if(mini > num):
                mini = min(num, mini)
                maxi = float('-inf')
            maxi = max(num, maxi)
            total = max(maxi-mini, total)
        return total

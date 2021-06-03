class Solution(object):
    def mincostTickets(self, days, costs):
        last_day = days[-1]
        days = set(days)
        dp = [0 for _ in range(last_day+1)]

        for i in range(1, last_day+1):
            if i not in days:
                dp[i] = dp[i-1]
                continue
            dp[i] = min(dp[i-1] + costs[0],
                        min(
                dp[max(i-7, 0)] + costs[1],
                dp[max(i-30, 0)] + costs[2]
            )
            )
        return dp[-1]

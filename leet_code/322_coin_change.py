class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ref = [float("inf") for _ in range(amount + 1)]
        ref[0] = 0

        for denom in coins:
            for i in range(amount + 1):
                if denom <= i:
                    ref[i] = min(ref[i], ref[i-denom] + 1)
        return ref[-1] if ref[-1] != float("inf") else -1

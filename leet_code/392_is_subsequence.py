class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            while j < len(t) and t[j] != s[i]:
                j += 1
            if j < len(t) and t[j] == s[i]:
                j += 1
                i += 1

        return i == len(s)

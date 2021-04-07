class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        first, second = s[:half], s[half:]
        ref = set("a e i o u".split())
        count_first, count_second = 0, 0
        for i, char in enumerate(first):
            sec = second[i]
            if(sec.lower() in ref):
                count_second += 1
            if(char.lower() in ref):
                count_first += 1

        return count_second == count_first

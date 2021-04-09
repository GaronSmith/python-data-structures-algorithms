class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1:
            return True
        ref = {}
        for i, x in enumerate(order):
            ref[x] = i
        idx = 0
        while idx < len(words)-1:
            first = words[idx]
            second = words[idx+1]
            length = len(first) if len(first) <= len(second) else len(second)
            flag = False
            for i in range(length):
                char1 = first[i]
                char2 = second[i]
                print(ref[char1], ref[char2])
                if ref[char1] > ref[char2]:
                    return False
                elif ref[char1] < ref[char2]:
                    flag = True
                    break
            if not flag and len(first) > length:
                return False
            idx += 1
        return True

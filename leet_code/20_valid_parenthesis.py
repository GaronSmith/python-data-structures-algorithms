class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        ref = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in ref:
                if stack:
                    cur = stack.pop()
                    if cur != ref[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False

        return True

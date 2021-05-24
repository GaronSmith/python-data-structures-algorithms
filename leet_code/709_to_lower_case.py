class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ""
        for val in str:
            if ord(val) >= 65 and ord(val) <= 90:
                res += chr(ord(val)+32)
            else:
                res += val

        return res

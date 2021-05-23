class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        directions = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
        for char in moves:
            pos[0] += directions[char][0]
            pos[1] += directions[char][1]
        return pos[0] == 0 and pos[1] == 0

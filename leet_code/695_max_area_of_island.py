  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
       def search(coord):

            if(grid[coord[0]][coord[1]] == 0):
                return 0

            stack = [coord]
            area = 0

            while stack:
                curr = stack.pop()
                if curr not in ref:
                    ref.add(curr)
                    if grid[curr[0]][curr[1]] == 1:
                        area += 1
                        if (curr[0]-1 >= 0):
                            stack.append((curr[0]-1, curr[1]))
                        if (curr[0]+1) < len(grid):
                            stack.append((curr[0]+1, curr[1]))
                        if curr[1]-1 >= 0:
                            stack.append((curr[0], curr[1]-1))
                        if (curr[1]+1 < len(grid[0])):
                            stack.append((curr[0], curr[1]+1))
            return area

        ref = set()
        maxi = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row, col) not in ref:
                    temp = search((row, col))
                    maxi = max(temp, maxi)
        return maxi

def hourglassSum(arr):

    row, col = 0, 0
    ans = float("-inf")
    while row <= 3:
        col = 0
        while col <= 3:
            end = col + 2
            top = sum([arr[row][col], arr[row][col+1], arr[row][col+2]])
            middle = arr[row+1][col+1]
            bottom = sum([arr[row+2][col], arr[row+2]
                          [col+1], arr[row+2][col+2]])
            hour_sum = sum([top, middle, bottom])
            ans = max(hour_sum, ans)
            col += 1
        row += 1

    return ans

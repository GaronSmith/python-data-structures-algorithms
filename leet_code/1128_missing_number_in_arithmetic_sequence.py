class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        dif = abs(arr[0] - arr[-1])
        change = dif / len(arr)

        for i, num in enumerate(arr[:-1]):
            if abs(num - arr[i+1]) != change:
                if num < arr[i+1]:
                    return int(num + change)
                else:
                    return int(num - change)
            elif num == arr[i+1]:
                return num

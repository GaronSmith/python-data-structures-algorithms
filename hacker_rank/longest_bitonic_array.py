def longestBitonicSubarray(arr):
    # Write your code here
    i = 1
    ans = 0
    while i < len(arr) - 1:
        j, k = i-1, i+1
        left, curr, right = arr[j], arr[i], arr[k]
        if(left <= curr and curr >= right):
            while j >= 0 and arr[j] >= arr[j-1]:
                j -= 1
            while k < len(arr)-2 and arr[k] >= arr[k+1]:
                k += 1
            diff = k-j + 1
            ans = max(ans, diff)
        elif(i == 1 and left >= curr and curr >= right):
            while i < len(arr) - 1 and arr[i] >= arr[i+1]:
                print(arr[i], arr[i+1])
                i += 1
            ans = max(ans, i+1)
        elif(i == 1 and left >= curr and curr >= right):
            while i < len(arr) - 1 and arr[i] <= arr[i+1]:
                i += 1
            ans = max(ans, i + 1)

        i += 1
    return ans

# nto 100% 
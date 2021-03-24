def binarySearch(array, target):
    # Write your code here.
    start, mid, end = 0, (len(array)-1)//2, len(array) - 1


    while start <= end:
            mid = (start + end) // 2
            if target > array[mid]:
                start = mid + 1
            elif target < array[mid]:
                end = mid - 1
            else:
                return mid

        return -1

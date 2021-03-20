arr = [1,2,-4,-6,8,-5,2,3,-6,3,-2]

def cross_sub_array(arr, low, mid, high):
    right_sum = left_sum = float('-inf')
    total = 0 
    max_right, max_left = mid+1, mid
    for i in range(mid,low, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i
    total =0
    for j in range(mid+1, high):
        total += arr[j]
        if total > right_sum:
            right_sum = total
            max_right = j
    
    return (max_left, max_right, left_sum+right_sum)

def max_sub_array(arr, low, high ):
    print(low, high)
    if high <= low:
        return (low, high, arr[low])
    mid = (high-low) // 2

    left_low, left_high, left_sum = max_sub_array(arr, low, mid)
    right_low, right_high, right_sum = max_sub_array(arr, mid+1, high)
    cross_low, cross_high, cross_sum = cross_sub_array(arr, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    else:
        return (cross_low,cross_high, cross_sum)


print(max_sub_array(arr, 0, len(arr)-1))




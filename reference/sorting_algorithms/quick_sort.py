def quick_sort(input_list):
    n = len(input_list)
    if(n <=1): return input_list
    pivot = input_list[0]
    left = list()
    right = list()
    for i in range(1,n):
        curr = input_list[i]
        if(curr > pivot):
            right.append(curr)
        else:
            left.append(curr)

    left = quick_sort(left)
    right = quick_sort(right)
    return [*left,pivot,*right]


print(quick_sort([1,3,2,7,9,5,6,3]))
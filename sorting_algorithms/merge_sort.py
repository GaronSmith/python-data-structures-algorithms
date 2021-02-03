def merge(l,r):
    merged = []
    pointer_l = 0
    pointer_r = 0
    while pointer_l < len(l) and pointer_r < len(r):
        if(l[pointer_l] <= r[pointer_r]):
            merged.append(l[pointer_l])
            pointer_l +=1
        else:
            merged.append(r[pointer_r])
            pointer_r += 1
    
    merged += r[pointer_r:]
    merged += l[pointer_l:]
    return merged


def merge_sort(input_list):
    if (len(input_list) == 1):
        return input_list
    
    m = round(len(input_list)/2)
    left = merge_sort(input_list[:m])
    right = merge_sort(input_list[m:])

    return merge(left,right)


print(merge_sort([1,4,2,7,8,4,0,5]))
def insertion_sort(input_list):
    for i in range(1,len(input_list)):
        value = input_list[i]
        idx = i
        while value > input_list[idx - 1] and idx>0: #change < to > for non increaseing 
            input_list[idx] = input_list[idx-1]
            idx -= 1
        input_list[idx] = value
    
    return input_list

print(insertion_sort([1,5,3,8,6,3,9,10]))
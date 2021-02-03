def swap(input_list, idx1, idx2):
    input_list[idx2], input_list[idx1] = input_list[idx1], input_list[idx2]

def selection_sort(input_list):
    n = len(input_list)
    for i in range(n):
        min_idx = i
        for j in range(i,n):
            if(input_list[min_idx] > input_list[j]):
                min_idx = j
        if(min_idx != i):
            swap(input_list, min_idx, i)
        
    return input_list

print(selection_sort([1,4,32,7,4,9,3]))
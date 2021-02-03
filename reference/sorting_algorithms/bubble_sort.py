def swap(input_list, idx1, idx2):
    input_list[idx2], input_list[idx1] = input_list[idx1], input_list[idx2]

def bubble_sort(input_list):
    n = len(input_list)
    swapped = False

    while (not swapped):
        swapped = True
        for i in range(1,n):
            bubble_val = input_list[i-1]
            comp_val = input_list[i]
            if(bubble_val > comp_val):
                swap(input_list, i-1, i)
                swapped = False
    return input_list


print(bubble_sort([1,4,3,6,7,3,9]))

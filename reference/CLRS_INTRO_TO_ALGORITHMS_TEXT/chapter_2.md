### 2.1.1 illustrate insertion sort
* ![alt text](../Static/InsertionSort.gif)

### 2.1.2 re-write insertion sort to non-increasing rather than non-decreasing 
* change < to > in while loop
```
def insertion_sort(input_list):
        for i in range(1,len(input_list)):
        value = input_list[i]
        idx = i
        while value > input_list[idx - 1] and idx>0: 
            input_list[idx] = input_list[idx-1]
            idx -= 1
        input_list[idx] = value
    
    return input_list
```

### 2.1.3 right a linear search implementing a loop invariant
```
def linear_search(a, v):
    for item in a:
        if item == v:
            return item
    return None
```

### 2.1.4  state the problem for adding two n-bit integers stored in two n-length arrays 

* input: two arrays(A and B) representing an integer in binary format where each digit is 0,1 with the length of n-bits
* output: an array represnting an integer in binary format such that C = A + B where A B C are the integers representation fo the array 
* python code
```
def add_binary(A, B):
    C = [None]  * len(A)+1
    carry = 0
    for i in len(A):
        C[i] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) /2
    C[i] = carry
    return C 
```

### 2.2.1 express n^3/1000 - 100n^2 - 100n +3 in Onotation 
* On^3

### 2.2.2 what is the loop invariant of selection sort, why only need to run n-1 times what is the run time, 

* code :
```
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

```
* loop invariant: all items to the left of selected index list[0:i-1] are sorted and each loop finds the smallest number on the right. 
* only need n-1 because all items to the left of penultimate value are sorted and there is only one value to the right which by definition is the greatest value 
* run time worst case n^2

### 2.2.3 how many items need to be checked on average, what is best and worst case?

* best case average = half worst case is all both are O(n)

### 2.2.4 how can we modify almost any algo to have a good best-case running time?
* if we optimize for best-case efficiently 

### 2.3.1 illustrate merge sort 
* ![alt text](../Static/MergeSort.gif)

### 2.3.2 write merge sort without sentinels
```
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
```

### 2.3.3 use mathmatical induction to show that 
* tbd 


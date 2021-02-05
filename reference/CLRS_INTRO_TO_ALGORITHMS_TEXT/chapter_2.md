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
'''
def linear_search(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return None
'''

### 2.1.4  state the problem for adding two n-bit integers stored in two n-length arrays 

* input: two arrays(A and B) representing an integer in binary format where each digit is 0,1 with the length of n-bits
* output: an array represnting an integer in binary format such that C = A + B where A B C are the integers representation fo the array 
* python code
'''
def add_binary(A, B):
    C = [None]  * len(A)+1
    carry = 0
    for i in len(A):
        C[i] = (A[i] + B[i] + carry) % 2
        carry = (A[i] + B[i] + carry) /2
    C[i] = carry
    return C 
'''
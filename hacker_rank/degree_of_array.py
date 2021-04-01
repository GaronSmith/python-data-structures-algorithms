from collections import defaultdict


def degreeOfArray(arr):
    ref = defaultdict(list)
    for i, num in enumerate(arr):
        ref[num].append(i)
    ref2 = defaultdict(int)
    max_num = 0
    for key in ref:
        max_num = max(len(ref[key]), max_num)
    min_dist = float("inf")
    for key in ref:
        if(len(ref[key]) == max_num):
            min_dist = min(min_dist, ref[key]
                           [len(ref[key])-1] - ref[key][0] + 1)
    return min_dist

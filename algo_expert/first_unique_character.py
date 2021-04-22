
def first_unique(string):
    ref = {}
    for i,char in enumerate(string):
        if char in ref:
            ref[char][0] = i
            ref[char][1] += 1
        else:
            ref[char] = [i, 1]
    for key in ref:
        if ref[key][1] == 1 : return ref[key][0]
    
    return -1 
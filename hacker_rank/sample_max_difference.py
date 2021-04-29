def maxDifference(px):
    # Write your code here
    ref = [-1 for _ in px[1:]]
    mini = px[0]
    for i, price in enumerate(px[1:]):
        dif = price - mini if price - mini > 0 else -1
        mini = min(mini, price)
        ref[i] = max(ref[i-1], dif)
    return ref[-1]

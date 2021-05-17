from collections import defaultdict


def mostFrequentDigits(a):
    ref = defaultdict(int)
    maxi = float("-inf")
    for num in a:
        if num < 10:
            ref[num] += 1
            maxi = max(maxi, ref[num])
        else:
            ten = num // 10
            left = num % 10
            ref[ten] += 1
            ref[left] += 1
            maxi = max(maxi, ref[ten], ref[left])
    ans = []
    for key in ref:
        if ref[key] == maxi:
            ans.append(key)

    return sorted(ans)


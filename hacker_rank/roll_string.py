def rollTheString(s, roll):
        ans = [x for x in s]
        ref = {idx:0 for idx,y in enumerate(s)}
        ref_num = {}
        for num in roll:
            if num in ref_num:
                ref_num[num] +=1
            else:
                ref_num[num] = 1

        for key in ref_num:
            for i in range(key):
                ref[i] += ref_num[key]
        for idx in ref:
             ans[idx] = chr(((ord(ans[idx]) + - (97- ref[idx])) % 26) + 97)
        return "".join(ans)

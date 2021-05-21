def mergeOverlappingIntervals(intervals):
    # Write your code here.
	intervals = sorted(intervals, key=lambda x: x[0])

	ans = []
	current_interval = intervals[0]
	ans.append(current_interval)
	for nxt in intervals:
		_, end = current_interval
		nxt_start, nxt_end = nxt

		if end >= nxt_start:
			current_interval[1] = max(end, nxt_end)
		else:
			current_interval = nxt
			ans.append(current_interval)

	return ans

def minimumWaitingTime(queries):
    queries.sort()


total_waiting = 0
	length = len(queries)
	for i, dur in enumerate(queries):
		queries_left = length - (i + 1)
		total_waiting += dur * queries_left
    return total_waiting

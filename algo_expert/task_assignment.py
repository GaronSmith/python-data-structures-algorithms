from collections import defaultdict


def taskAssignment(k, tasks):
    # Write your code here.
	ref = defaultdict(lambda: [])
	for i, num in enumerate(tasks):
		ref[num].append(i)
	tasks.sort()
	length = len(tasks) - 1
	ans = []
	for i in range(k):
		dur = tasks[i]
		ans.append([ref[dur].pop(), ref[tasks[length - i]].pop()])

    return ans

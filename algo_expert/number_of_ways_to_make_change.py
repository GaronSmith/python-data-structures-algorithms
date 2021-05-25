def numberOfWaysToMakeChange(n, denoms):
	coins = [0 for _ in range(n+1)]
	coins[0] = 1
	for num in denoms:
		for i in range(len(coins)):
			if(num <= i):
				coins[i] += coins[i-num]
	return coins[n]
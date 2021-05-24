def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    number_of_coins = [float("inf") for _ in range(n + 1)]


number_of_coins[0] = 0
for denom in denoms:
		for num in range(len(number_of_coins)):
			if denom <= num:
				number_of_coins[num] = min(
				    number_of_coins[num], 1 + number_of_coins[num - denom])
	return number_of_coins[n] if number_of_coins[n] != float("inf") else -1

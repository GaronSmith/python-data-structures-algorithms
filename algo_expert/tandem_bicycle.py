def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort(reverse=fastest)
	total = 0
	for i, j in zip(blueShirtSpeeds, redShirtSpeeds):
		total += max(i, j)
    return total

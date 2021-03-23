def kadanesAlgorithm(array):
    # Write your code here.
    max_here = array[0]
    max_sofar = array[0]
    for num in array[1:]:
            max_here = max(num, max_here+num)
            max_sofar = max(max_sofar, max_here)

        return max_sofar

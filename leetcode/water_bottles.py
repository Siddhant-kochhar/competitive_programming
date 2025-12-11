numBottles = 15
numExchange = 4

total = numBottles
empty = numBottles

while empty >= numExchange:
	new_bottles = empty // numExchange
	total += new_bottles
	empty = empty % numExchange + new_bottles

print(total)
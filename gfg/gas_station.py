'''
Input: gas[] = [4, 5, 7, 4], cost[]= [6, 6, 3, 5]
Output: 2
Explanation: Start at gas station at index 2 and fill up with 7 units of gas. Your tank = 0 + 7 = 7
Travel to station 3. Available gas = (7 – 3 + 4) = 8.
Travel to station 0. Available gas = (8 – 5 + 4) = 7.
Travel to station 1. Available gas = (7 – 6 + 5) = 6.
Return to station 2. Available gas = (6 – 6) = 0.
'''
gas = [4, 5, 7, 4]
cost= [6, 6, 3, 5]



max_gas = max(gas)
max_index_gas = gas.index(max_gas)
initial_gas = max_gas

while initial_gas > 0:
    next_index = (max_index_gas + 1 )%len(gas)
    initial_gas = initial_gas - gas[max_index_gas] + cost[next_index]

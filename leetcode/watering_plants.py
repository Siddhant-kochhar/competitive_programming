plants = [2,2,3,3]
capacity = 5

def watering_plants(plants, capacity):
    water = capacity
    steps = 0
    for i in range(len(plants)):
        if water < plants[i]:
            steps += 2 * i
            water = capacity
        water -= plants[i]
        steps += 1
    return steps

print(watering_plants(plants, capacity))
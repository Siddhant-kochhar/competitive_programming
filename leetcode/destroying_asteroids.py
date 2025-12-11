mass = 5
asteroids = [4,9,23,4]


asteroids.sort(reverse=True)
temp = []

for asteroid in asteroids:
    if mass >= asteroid:
        mass += asteroid
    else:
        temp.append(asteroid)
    

temp.sort()

for asteroid in temp:
    if mass >= asteroid:
        mass += asteroid
    else:
        print(False)
        break
else:
    print(True)

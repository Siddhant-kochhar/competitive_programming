# Predefined score matrix representing the target's rings
score = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1]
]

t = int(input())
for _ in range(t):
    a = []
    for _ in range(10):
        s = input()
        a.append(list(s))

    total_score = 0
    for i in range(10):
        for j in range(10):
            if a[i][j] == 'X':
                total_score += score[i][j]
    print(total_score)
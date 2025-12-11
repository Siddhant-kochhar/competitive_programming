points = [[1,0],[0,0],[0,1]]
area = float("-inf")

def calculate_area(x1,x2,x3,y1,y2,y3):
    area = (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area

n = len(points)
for i in range(n):
    for j in range(i,n):
        for k in range(j,n):
            x1 = points[i][0]
            x2 = points[j][0]
            x3 = points[k][0]

            y1 = points[i][1]
            y2 = points[j][1]
            y3 = points[k][1]


        area = max(area,calculate_area(x1,x2,x3,y1,y2,y3))
print(area)
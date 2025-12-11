date = "20th Oct 2052"
x = date.split()
print(x)

map = {
    "Jan":1,
    "Feb":2,
    "Mar":3,
    "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12
    }

date = x[0][:2]
month = map[x[1]]
year = x[2]

print(str(year)+"-"+str(month)+"-"+(date))
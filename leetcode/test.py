# s = "hello"
# seen = set()

# for i in s:
#     if i in seen:
#         print(i)
#         break
#     seen.add(i)

nums = [2,7,11,15]
target = 9
seen = {}

for i,j in enumerate(nums):
    if target-j in seen:
        print(seen[target-j],i)
        break
    seen[j] = i 


x = [1,2,3,4,5,6,7,8]

for i in range(0,len(x)//2,2):
    x[i],x[i+1] = x[i+1],x[i]
print(x)

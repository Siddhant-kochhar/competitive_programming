'''
2
123
78
130
10
0	2	
Initial experience level is 123 points.
Defeat the first monster having power of 78 and bonus of 10. Experience level is now 123+10=133.
Defeat the second monster.
'''



# initial_power = 100
# monster = [101,100,304]
# power  = [100,1,524]
# combined = []


# for i,j in zip(monster,power):
#     combined.append((i,j))

# print(combined)


# combined.sort(key = lambda x:x[1],reverse = True)
# print(combined)

# cnt = 0 
# for p,b in combined:
#     if p <= initial_power:
#         cnt += 1 
#         initial_power += b

#     else:
#         break
# print(cnt)



monster = [101,100,304]
power  = [100,1,524]


combined = []

for i,j in zip(monster,power):
    combined.append((i,j))

print("Normal Combined",combined)

nums = combined.copy()
nums = sorted(nums,key=lambda x:x[0])

print("Sorted using first value and in ascending order",nums)

nums = sorted(nums,key=lambda x:x[0],reverse = True) 
print("Sorted using first value and in descending order",nums)

nums = sorted(nums,key=lambda x:x[1])
print("Sorted using second value and in ascending order",nums)

nums = sorted(nums,key=lambda x:x[1],reverse = True)
print("Sorted using second value and in descending order",nums)




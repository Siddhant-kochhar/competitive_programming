'''
if version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
'''


version1 = "1.2"
version2 = "1.10"

version_list_one = version1.split(".")
print(version_list_one)

version_list_two = version2.split(".")
print(version_list_two)

l = 0 
while l < len(version_list_one) or l < len(version_list_two):
    v1 = int(version_list_one[l]) if l < len(version_list_one) else 0
    v2 = int(version_list_two[l]) if l < len(version_list_two) else 0
    if v1 < v2:
        print(-1)
        break
    elif v1 > v2:
        print(1)
        break
    else:
        l += 1
else:
    print(0)

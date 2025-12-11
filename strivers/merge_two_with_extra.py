nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

i = 0 
j = 0 
while i < len(nums1) or j < len(nums2):
    if nums1[i] > nums2[j]:
        nums1[i],nums2[j] = nums2[j],nums1[i]
        i += 1 
    else:
        

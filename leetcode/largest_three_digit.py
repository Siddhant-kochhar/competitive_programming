# num = "6777133339" 
# num_list = list(num)
# max_num = float('-inf')

# i = 0 
# for j in range(len(num)):
#     # Check if we have a valid 3-digit window
#     if j - i + 1 == 3:
#         x = int(''.join(num_list[i:j+1]))
#         if x > max_num:
#             max_num = x
#         i += 1  # Slide the window

# print(f"The largest 3-digit number is: {int(max_num)}") 
from collections import Counter

num = "6777133339" 
num_list = list(num)
num_dict = Counter(num_list)
candidate = []

for key,value in num_dict.items():
    if value >=3:
        candidate.append(key)

candidate.sort(reverse=True)
if candidate:
    print(candidate[0]*3)



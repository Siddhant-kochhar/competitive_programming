'''
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd'
are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
'''

s = "lEetcOde"
s_list = list(s)

vowels = ["a","e","i","o","u","A","E","I","O","U"]

position = []
vowels_found = []

for i,j in enumerate(s_list):
    if j in vowels:
        position.append(i)
        vowels_found.append(j)

print(position)
vowels_found = sorted(vowels_found)

p = 0
for t in position:
    s_list[t] = vowels_found[p]
    p+=1

print("".join(s_list))

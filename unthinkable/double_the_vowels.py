'''
Input : Sequoia
Output : Seequuooiiaa
'''

vowels = "aeiouAEIOU"
x = "Sequoia"
res =""
for i in x:
    if i in vowels:
        res += (i * 2)
    else:
        res += i 

print(res)
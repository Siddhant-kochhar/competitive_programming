'''
Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"
'''
address = "1.1.1.1"
address_split = address.split(".")
print(address_split)
res = "[.]".join(address_split)
print(res)

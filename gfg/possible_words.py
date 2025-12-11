from itertools import product

num = {
    2 :"abc",
    3:"def",
    4:"ghi",
    5:"jkl",
    6:"mno",
    7:"pqqrs",
    8:"tuv",
    9:"wxyz"
}

arr = [2, 3]
letters = [num[i] for i in arr]
print((letters))

# Generate all possible words
words = set("".join(p) for p in product(*letters))
print(list(words))
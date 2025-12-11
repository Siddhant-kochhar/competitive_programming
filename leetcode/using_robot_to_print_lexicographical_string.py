s = "zza"
t = []
paper = ""

for ch in s:
    while t and t[-1] > ch:
        paper += t.pop()
    t.append(ch)

# add stack in order
paper += "".join(t)

print(paper)  # azz

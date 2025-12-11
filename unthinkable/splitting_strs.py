s = "codingninjas"

n = len(s)
part1 = s[:n//2]
part2 = s[n//2:]

def check(part1,part2):
    vowels = "aeiou"
    count1 = sum(1 for char in part1 if char in vowels)
    count2 = sum(1 for char in part2 if char in vowels)
    
    return count1 == count2

print(check(part1,part2))
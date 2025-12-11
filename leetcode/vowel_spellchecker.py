'''
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
'''

wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]

def tolower(c:str) -> str:
    return c.lower()

def isvowel(s:str) -> str:
    return s in "aeiou"

def maskvowels(c:str) -> str:
    return "".join("*" if isvowel(c) else c for c in s)


exact_set = set()
case_map = {}
vowel_map = {}

for word in wordlist:
    exact_set.add(word)

    lower_word = tolower(word)
    case_map.setdefault(lower_word,word)
    masked_word = maskvowels([lower_word])
    vowel_map.setdefault(masked_word,word)

def check_for_match(query:str) -> str:
    if query in exact_set:
        return query
    lower_query = tolower(query)
    if lower_query in case_map:
        return case_map[lower_query]
    
    masked_query = maskvowels(lower_query)


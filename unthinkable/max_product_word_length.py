words = ["abcw","baz","foo","bar","xtfn","abcdef"]
n = len(words)
words_set = [set(words[i]) for i in range(n)]
print(words_set)
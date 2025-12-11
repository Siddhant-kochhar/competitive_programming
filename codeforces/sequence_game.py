'''
Tema and Vika are playing the following game.

First, Vika comes up with a sequence of positive integers a
 of length 𝑚
 and writes it down on a piece of paper. Then she takes a new piece of paper and writes down the sequence b
 according to the following rule:

First, she writes down ai
.
Then, she writes down only those ai
 (2≤𝑖≤𝑚
) such that ai-1≤ai
. Let the length of this sequence be denoted as n
.
For example, from the sequence a =[4,3,2,6,3,3]
, Vika will obtain the sequence b =[4,6,3]
.

She then gives the piece of paper with the sequence b
 to Tema. He, in turn, tries to guess the sequence a
.

Tema considers winning in such a game highly unlikely, but still wants to find at least one sequence a
 that could have been originally chosen by Vika. Help him and output any such sequence.
'''
b = [1,7,9,5,7]

a = [b[0]]

for i in range(1, len(b)):
    if b[i] >= b[i-1]:
        a.append(b[i])
    else:
        a.append(b[i])
        a.append(b[i])

print(len(a))
print(a)
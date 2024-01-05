# Given a string s, find the length of the longest
# substring
# without repeating characters.
s = 'appabappachappa'
s = 'supercalifragilisticexpicalidacious'
import numpy as np

def check_unique(string):
    if len(list(set(string))) == len(string):
        return len(string)
    return 0

def longest_non_rep(s):
    dim = len(s) + 1
    final = np.zeros((dim,dim))
    for i in range(dim):
        for j in range(dim):
            final[i,j] = check_unique(s[i:j])
    indices = np.unravel_index(final.argmax(), final.shape)

    return s[indices[0]:indices[1] ]


print(longest_non_rep(s))
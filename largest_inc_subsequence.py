sequence = [1,3,2,4,4.3,5,6,7,8,234,43,5,345,234,345,236,341245,46,54,6143,512,34,1234,125,345,32,5,2345,45,234]
seque = sequence + sequence
# larrgest increasing subarray, via the sliding window
import numpy as np
sequence = np.array(sequence)

def max_inc_subarray(sequence):
    max_l = len(sequence)
    if sequence[1] > sequence[0]:
        right = 1
        left = 0
        best = 1
    else:
        left = 1
        right = 1
        best = 0
    while left < max_l and right < max_l:
        if sequence[right] >= sequence[right - 1]:
            right = right + 1
            if best <right - left + 1:
                best = right - left 
                print(sequence[left:right ])
        else:
            right = right + 1
            left = right
    return best
# print(max_inc_subarray(sequence))
# largest increasing subsequence now
# sequence = np.array([4.3,5,6,7,8,234,9,5,43])
def larg_inc_subseq_slow(sequence):
    if np.array([]).shape == sequence.shape:
        return 1
    first_elemt = sequence[0]
    rests = np.array(sequence[np.argwhere(sequence > first_elemt).squeeze()])
    if rests.size  == 1:
        return 1
    temp1 = larg_inc_subseq_slow(rests)+1
    temp2 = larg_inc_subseq_slow(sequence[1:])
    return max(temp1, temp2)

print(larg_inc_subseq_slow(sequence))
print(len(sequence))
# memo it
def larg_inc_subseq(sequence,memo = {}):
    if sequence.tobytes() in memo:
        return memo[sequence.tobytes()]
    if np.array([]).shape == sequence.shape:
        memo[sequence.tobytes()] = 1
        return 1
    first_elemt = sequence[0]
    rests = np.array(sequence[np.argwhere(sequence > first_elemt).squeeze()])
    if rests.size  == 1:
        memo[rests.tobytes()] = 1
        return 1
    temp1 = larg_inc_subseq(rests)+1
    temp2 = larg_inc_subseq(sequence[1:])
    memo[sequence.tobytes()] =  max(temp1, temp2)
    return memo[sequence.tobytes()] 

import cProfile
import re
cProfile.run('larg_inc_subseq(sequence)')
cProfile.run('larg_inc_subseq_slow(sequence)')

# checked the profling results, memos make everything crazy fast
#WoW!
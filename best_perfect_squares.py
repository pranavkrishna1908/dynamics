# one thing is that I can just make a list and use the best_sum from before
# write bestsum again?
# how to improve the best_sum apraoch?
import numpy as np
# def best_sum (target):
#     num = np.floor(np.sqrt(target))
#     nums_list = np.arange(1, num + 1)**2
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     best_so_far = list(np.ones(int(target)))
#     for item in nums_list:
#         temp = best_sum(target - item)
#         if temp is not None:
#             if len(best_so_far) > len(temp):
#                 best_so_far = temp + [item]
#     return best_so_far
def best_sum (target, memo = {}):
    num = np.floor(np.sqrt(target))
    nums_list = np.arange(1, num + 1)**2
    if target == 0:
        return []
    if target < 0:
        return None
    if target in memo:
        return memo[target]
    best_so_far = list(np.ones(int(target)))
    for item in nums_list:
        temp = best_sum(target - item, memo)
        if temp is not None:
            if len(best_so_far) > len(temp):
                best_so_far = temp + [item]
    memo [ target] =  best_so_far
    return memo [ target]
print(best_sum(906))
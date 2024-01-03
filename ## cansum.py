# ## cansum
# def cansum(target, num_list):
#     if target == 0:
#         return True
#     if target <0:
#         return False
#     temp = 0
#     for item in num_list:
#         temp = temp + cansum(target - item, num_list)
#     return temp > 0
# print(cansum(542,[3,5,7,89,34,62]))
# perfect!
# now, memo making stuff
# def cansum2(target, num_list, memo = {}):
#     if target == 0:
#         return True
#     if target <0:
#         return False
#     if target in memo:
#         return memo[target]
#     temp = 0
#     for item in num_list:
#         temp = temp + cansum2(target - item, num_list, memo)
#     memo[target] =  temp > 0
#     return memo[target]
# print(cansum2(542,[3,5,7,89,34,62]))
# but how?write another program to return the way


    

    
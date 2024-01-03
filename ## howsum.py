## howsum
# def howsum(target, num_list):
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     for item in num_list:
#         temp = howsum(target - item, num_list)
#         if temp != None:
#             temp = temp + [item]
#             return temp# this return is important, otherwise, I will over-write the results from the previous function calls, all the time
#     return temp
# print(howsum(1542,[93,5,7,89,34,62]))
# we improve it now
def howsum2(target, num_list, memo = {}):
    if target == 0:
        return []
    if target <0:
        return None
    if target in memo:
        return memo[target]
    for item in num_list:
        temp = howsum2(target - item, num_list, memo)
        if temp != None:
            memo[target] =  temp + [item]
            return memo[target]
print(howsum(1542,[93,5,7,89,34,62]))
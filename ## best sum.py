## best sum
# def bestsum(target, num_list):
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     min = [1,2,3,4,5,6,7,34,2345,2345,23,45,35,45,2,34,325,5,5,2345,234,5,2345,34,5,3245,32,5423,45]
#     for item in num_list:
#         temp = bestsum(target - item, num_list)
#         if temp != None:
#             if len(min) > len(temp):
#                 min =  temp + [item]
#     return min
# print(bestsum(93+7+34,[93,5,7,89,34,62]))

def bestsum(target, num_list, memo = {}):
    if target == 0:
        return []
    if target < 0:
        return None
    if target in memo:
        return memo[target]
    min = [1,2,3,4,5,6,7,34,2345,2345,23,45,35,45,2,34,325,5,5,2345,234,5,2345,34,5,3245,32,5423,45]
    for item in num_list:
        temp = bestsum(target - item, num_list,memo)
        if temp != None:
            if len(min) > len(temp):
                min =  temp + [item]
    memo[target] =  min
    return min
print(bestsum(145,[93,5,7,89,34,62]))


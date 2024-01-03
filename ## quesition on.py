## quesition on
# house robber in https://www.youtube.com/watch?v=_i4Yxeh5ceQ
my_list = [1,2,5,4,3,2,4,3,2,1,4,5,2,4]
my_list = [1,2,3,1]

def best_loot(my_list):
    if len(my_list) == 2:
        return max(my_list)
    if len(my_list) == 1:
        return my_list[0]
    temp = max(best_loot(my_list[1:]), my_list[0] + best_loot(my_list[2:]))
    return temp

print(best_loot(my_list))
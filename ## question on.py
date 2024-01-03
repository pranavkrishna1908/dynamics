## question on 
#house robber 2
# from https://www.youtube.com/watch?v=_i4Yxeh5ceQ

my_list = [1,2,5,4,3,2,4,3,2,1,4,5,2,4]
my_list = [2,3,2,3,100]
def best_loot(my_list):
    if len(my_list) == 2:
        return max(my_list)
    if len(my_list) == 1:
        return my_list[0]
    temp = max(best_loot(my_list[1:]), my_list[0] + best_loot(my_list[2:]))
    return temp

def best_loot_circular(my_list):
    if len(my_list) == 3:
        return max(my_list)
    if len(my_list) == 4:
        return max(my_list[0] + my_list[2], my_list[1] + my_list[3])
    
    
    temp1 = my_list[0] + best_loot(my_list[2:-1])
    temp2 = my_list[-1] + best_loot(my_list[1:-3])
    temp3 = best_loot(my_list[1:-1])
    return max(temp1, temp2, temp3)
print(best_loot_circular(my_list))
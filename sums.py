target = 11
nums = [1,2,3,4,5]
def can_sum(target, nums):
    if target ==0:
        return 1
    if target < 1:
        return 0
    temp = 0
    for item in nums:
        temp = temp + can_sum(target - item, nums)
    return temp != 0
print(can_sum(target, nums))
def how_sum(target, nums):
    if target == 0:
        return []
    if target < 0:
        return None
    temp = []
    for item in nums:
        temp  = how_sum(target - item, nums)
        if temp is not None:
            temp =  temp + [item]
            return temp
print(how_sum(target, nums))

def best_sum(target, nums):
    if target == 0:
        return []
    if target < 0:
        return None
    min = []
    for item in nums:
        temp2 = best_sum(target - item, nums) 
        if temp2 is not None:
            temp2 = temp2 + [item]
            if len(temp2) < len(min) or min == []:
                min = temp2
    return min
print(best_sum(target, nums))

    

        
    
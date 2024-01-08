# because the array has the same thing twice, it needs to be even and the half of the sum is what is needed
nums = [1,5,11,5,6,6,90,90]
def howsum_slow(target, nums):
    if target == 0:
        return []
    if target < 0 or nums is None:
        return None
    answer = []
    for item in nums:
        temp1 = howsum_slow(target - item, list( filter(lambda element: element!=item,nums)))
        if temp1 is not None:
            answer = temp1 + [item]
            return answer

def partition_slow(nums):
    temp = sum(nums) 
    if temp %2==1:
        return None
    else:
        return howsum_slow(temp/2, nums)
    
def howsum(target, nums, memo = {}):
    if (target, nums) in memo:
        return memo[(target, nums)]
    if target == 0:
        return []
    if target < 0 or nums is None:
        return None
    answer = []
    for item in nums:
        temp1 = howsum(target - item, 
                       list( filter(lambda element: element!=item,nums)),
                       memo)
        if temp1 is not None:
            answer = temp1 + [item]
            memo[(target - item, 
                       list( filter(lambda element: element!=item,nums)))] = answer
            return answer
def partition(nums):
    temp = sum(nums) 
    if temp %2==1:
        return None
    else:
        return howsum(temp/2, nums)
import cProfile
import re
cProfile.run('partition_slow(nums)')
cProfile.run('partition(nums)')

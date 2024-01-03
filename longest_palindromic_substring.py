# from https://www.youtube.com/watch?v=_i4Yxeh5ceQ
# longest palindromic substring
# no idea how to proceedhere!!
# one hour later and unfortunately, too many things were wrong
def twoSum(nums, target):
    for num1 in range(len(nums)):
        for j in range(num1 + 1, len(nums)):
            temp = nums[num1] + nums[j]
            if  temp == target:
                return [num1,j]
            

print(twoSum([2,7,11,15], 9))
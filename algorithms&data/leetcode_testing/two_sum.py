def twoSum(nums, target):
    nums_dict = {}
    for i,num in enumerate(nums):
        complete = target - num
        if complete in nums_dict:
            return [nums_dict[complete], i]
        nums_dict[num] = i
    return []

print(twoSum(nums=[2, 7, 11, 15], target=9))
print(twoSum([3,2,4], target=6))
print(twoSum([3,3], target=6))
print(twoSum(nums=[2,5,5,11], target=10))
from networkx.classes import is_empty


def twoSum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        complete = target - num

        if complete in nums_dict:
            return [nums_dict[complete], i]
        
        nums_dict[num] = i

    return []

print(twoSum(nums=[2, 7, 11, 15], target=9))
print(twoSum([3,2,4], target=6))
print(twoSum([3,3], target=6))
print(twoSum(nums=[2,5,5,11], target=10))

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [i for i in list_1 if i % 2 == 0]

new_list = list(filter(lambda x: x % 2 == 0, list_2))


print(new_list)
print(list_2)

user_string = input().lower().replace(" ", "")

print(user_string is user_string[::-1])
# def nearest_value(nums, target):
#     if len(nums) == 0: return 'Error'
#     nums= list(nums)
#     distances_to_target = []
#     for num in nums:
#         distances_to_target.append(abs(target - num))
#     return nums[distances_to_target.index(min(distances_to_target))]

# print(nearest_value({4,7,10,11,12,17}, 9))
# print(nearest_value({4,7,10,11,12,17}, 8))
# print(nearest_value({1,2,3}, 8))
# print(nearest_value({100, 2}, 9))


# def first_word(text: str):
#     return text.split(' ')[0]

# print(first_word('Hello world python bye goodbye'))

# first_word('Hello world python bye goodbye')



# def is_acceptable_password(password):
#     return len(password) > 6

# print(is_acceptable_password('short'))
# print(is_acceptable_password('muchlonger'))

# def number_length(num: int):
#     return len(str(num)) 

# print(number_length(10))
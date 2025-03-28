users = ['a','b', 'c', 'd']
# users.append('e')
# users.extend('fghijklmno') # adds characters wise


users[2:2] = ['e', 'f']
print(users)
users[0:2] = ['g', 'h', 'I']
print(users)
# del users[0]
# print(users)
# users.clear()
# print(users)
# users.sort(key=str.lower)
# print(users)

nums = [4, 5, 65, 23]
# nums.reverse() # reverses the list
# print(nums)
# nums.sort(reverse=False) # descends the element orders inside list
# print(nums)
# # The above reverse methods reverses the orginal lists permanently. If we want temporarily we will use sorted.()
# print(sorted(nums, reverse=True))
# print(nums)
 # Copy
nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(nums)
print(nums_copy)
print(my_nums)
print(my_copy)
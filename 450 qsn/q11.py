def find(nums):
    l = len(nums)
    nums.sort()
    for i in range(0, l):
        if nums[i] == nums[i + 1]:
            return nums[i]
            break

nums = [2, 3, 1, 4, 5, 1, 6, 1]
print(find(nums))
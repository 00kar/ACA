class Solution:
    def findDisappearedNumbers(self,nums):
        return list(set(range(1, len(nums)+1))  - set(nums))

numbers = [4,3,2,7,8,2,3,1]
sol = Solution().findDisappearedNumbers(numbers)

print('given:', numbers)
print('filtered:', sol)

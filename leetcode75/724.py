#  Find Pivot Index
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sum_list = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sum_list[i + 1] = sum_list[i] + nums[i]
        print(sum_list)
        for i in range(len(nums)):
            if sum_list[i] == sum_list[-1]-sum_list[i+1]:
                return i

        return -1


nums = [1,2,3]
test = Solution()
print(test.pivotIndex(nums))

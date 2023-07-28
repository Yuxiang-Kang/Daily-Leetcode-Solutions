#Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k] = nums[i]
                k+=1

        for i in range(k,len(nums)):
            nums[i]=0

        return nums

nums = [0]
test = Solution()
new_nums = test.moveZeroes(nums)
print(new_nums)
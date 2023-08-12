# Longest Subarray of 1's After Deleting One Element
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = right = 0
        k = 1
        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1
            print(f"{nums[left:right+1]},k={k}")
        return right-left
nums = [1,1,1]
test=Solution()
print(test.longestSubarray(nums))
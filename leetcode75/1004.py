# Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        for i in range(len(nums), 0, -1):
            window_sum = sum(nums[0:i])
            if window_sum + k >= i:
                return i
            for j in range(1, len(nums) - i + 1):
                window_sum = window_sum + nums[j + i - 1] - nums[j - 1]
                # print(nums[j:j + i])
                if window_sum + k >= i:
                    # print(nums[j:j + i])
                    # print('yes!')
                    return i
        return 0


class Solution2:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # thought, use 2 pointers+window
        left = right = 0
        for right in range(len(nums)):
            if nums[right] ==0:
                k-=1
            if k<0:
                if nums[left]==0:

                    k+=1
                left+=1
            print(f"{nums[left:right+1]},k={k}")
        return right-left+1

nums = [1,1,1,0,0,0,1,1,1,1,0,0,0,0]
k = 2
test = Solution2()
print(test.longestOnes(nums, k))

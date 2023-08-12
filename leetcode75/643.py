# Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg = - float('inf')
        for i in range(len(nums) - k + 1):
            if sum(nums[i:i + k]) / k > avg:
                avg = sum(nums[i:i + k]) / k
        return avg


class Solution2(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_list = [0 for _ in range(len(nums) - k + 1)]
        print(sum_list)

        for i in range(len(nums) - k + 1):
            sum_list[i] = (sum(nums[i:i + k]))
        print(sum_list)
        return max(sum_list) / k


class Solution3(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum_list = [0 for _ in range(len(nums) - k + 1)]
        sum_list[0] = sum(nums[0:k])
        if len(nums) > k:
            for i in range(1, len(nums) - k + 1):
                sum_list[i] = sum_list[i - 1]-nums[i-1]+nums[i+k-1]
        print(sum_list)
        return max(sum_list) / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
test = Solution3()
print(test.findMaxAverage(nums, k))

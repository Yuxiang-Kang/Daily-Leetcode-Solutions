# Increasing Triplet Subsequence

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    for k in range(j + 1, len(nums)):
                        if nums[k] > nums[j]:
                            print(f'{nums[i]},{nums[j]},{nums[k]}')
                            return True
        return False


class Solution2(object):
    def increasingTriplet(self, nums):
        # inspired by https://blog.csdn.net/QuantumYou/article/details/120104612
        """
        algorithm: get first two numbers s(small) and m(medium). Then start from m, examine every number nums[i]=a.
        If a < s, a <--> s
        If s<a<m, a <--> m
        If a>m, get it!

        But after a<-->s, s comes after m?
            because m does not change, if a number > m occurs, it still holds with a former s before m.
        :param nums:
        :return:
        """

        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        init = False
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    s = nums[i]
                    m = nums[j]
                    init = True
                    break
            if init:
                break
        if not init:
            return False
        for i in range(len(nums)):
            if nums[i] <= s:
                s = nums[i]
            elif nums[i] <= m:
                m = nums[i]
            elif nums[i] > m:
                print(f"s:{s}, m:{m}, l:{nums[i]}")
                return True

        return False


class Solution3(object):
    def increasingTriplet(self, nums):
        # inspired by girikuncoro in leetcode
        s = float('inf')
        m = float('inf')
        for i in range(len(nums)):
            if nums[i] <= s:
                s = nums[i]
            elif nums[i] <= m:
                m = nums[i]
            elif nums[i] > m:
                return True
            print(f"s:{s}, m:{m}")
        return False


nums = [5, 4, 3, 2, 1, 6]
test = Solution3()
print(test.increasingTriplet(nums))

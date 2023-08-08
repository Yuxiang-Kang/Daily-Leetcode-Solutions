# Max Number of K-Sum Pairs
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # thought: go through the list to see if the element has a match
        count = 0
        i = 0
        while i < len(nums):
            print(f"i={i}")
            if nums[i] >= k:
                i += 1
                continue
            for j in range(i + 1, len(nums), 1):
                match = False
                if nums[i] + nums[j] == k:
                    print(f"{nums[i]}+{nums[j]}={k}")
                    nums.remove(nums[i])
                    nums.remove(nums[j - 1])
                    match = True
                    count += 1
                    print(nums)
                    break
            if match:
                continue
            i += 1
        return count


class Solution2(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # thought: split k into combinations of 2 numbers, then directly remove
        match = 0
        if max(nums) < int(k / 2):
            return 0
        for i in range(1, int(k / 2) + 1, 1):
            if nums.count(i) == 0 or nums.count(k - i) == 0:
                continue
            elif i == k / 2 and k % 2 == 0:
                match += int(nums.count(i) / 2)
                for j in range(2 * int(nums.count(i) / 2)):
                    nums.remove(i)
            else:
                match += min(nums.count(i), nums.count(k - i))
                for j in range(min(nums.count(i), nums.count(k - i))):
                    nums.remove(i)
                    nums.remove(k - i)
            print(f"{i}+{k - i}={k}")
            print(nums)
        return match


class Solution3(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Thought: Use 2 pointers. Before the process sort the list.
        nums.sort()
        i = 0
        j = len(nums) - 1
        match = 0
        while i < j:
            if nums[i] + nums[j] == k:
                match += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        print(nums)
        return match


nums = [1, 2, 3, 4, 2, 4, 1, 4, 3]
k = 5
test = Solution2()
print(test.maxOperations(nums, k))

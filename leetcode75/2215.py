# Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        def only_in_one_set(a, b):
            only_list = []
            for i in a:
                if (i not in b) and (i not in only_list):
                    only_list.append(i)
            return only_list

        only_nums1 = only_in_one_set(nums1, nums2)
        only_nums2 = only_in_one_set(nums2, nums1)
        print(only_nums1)
        print(only_nums2)
        print([only_nums1,only_nums2])
        return [only_nums1,only_nums2]


nums1 = [1,2,3,3]
nums2 = [1,1,2,2]
test = Solution()
print(test.findDifference(nums1, nums2))

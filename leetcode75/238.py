# Product of Array Except Self

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def ProductOfArray(arr):
            product = 1
            for i in range(len(arr)):
                product *= arr[i]
            return product
        product_nums = ProductOfArray(nums)
        answer = []
        for i in range(len(nums)):
            if nums[i] != 0:
                answer.append(int(product_nums / nums[i]))
            else:
                cut = nums[:]
                del cut[i]
                print(cut)
                print(ProductOfArray(cut))
                answer.append(ProductOfArray(cut))

        print(answer)
        return answer


nums = [-1,1,0,-3,3]
test = Solution()
test.productExceptSelf(nums)

# Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        sum_list = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            sum_list[i + 1] = sum_list[i] + gain[i]
        print(sum_list)
        return max(sum_list)


gain = [-4,-3,-2,-1,4,3,2]
test = Solution()
print(test.largestAltitude(gain))

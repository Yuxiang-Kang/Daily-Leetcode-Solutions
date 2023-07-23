class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        i = 0
        greatest = []
        while i < len(candies):
            new_candies = candies[:]
            new_candies[i] += extraCandies
            if new_candies[i] == max(new_candies):
                greatest.append(True)
            else:
                greatest.append(False)
            i += 1
        return greatest


class Solution2(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        i = 0
        current_max = max(candies)
        greatest = []
        while i < len(candies):
            if candies[i] + extraCandies >= current_max:
                greatest.append(True)
            else:
                greatest.append(False)
            i += 1
        return greatest


candies = [2, 3, 5, 1, 3]
extraCandies = 3
sol = Solution2()
G = sol.kidsWithCandies(candies, extraCandies)
print(G)

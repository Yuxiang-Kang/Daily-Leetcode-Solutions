# Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Thought: Decrease the width of the water and try every combination
        water = 0
        for i in range(len(height) - 1, 0, -1):
            print(f"i={i}")
            for j in range(0, len(height) - i):
                if min(height[j], height[j + i]) * i > water:
                    water = min(height[j], height[j + i]) * i
        return water


class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # only move the shorter end inside
        left_end = 0
        right_end = len(height) - 1
        water = []
        while 1:
            if left_end == right_end:
                break
            water.append(min(height[left_end], height[right_end]) * (right_end - left_end))
            if height[left_end] > height[right_end]:
                right_end -= 1
            else:
                left_end += 1
        return max(water)


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test = Solution2()
print(test.maxArea(height))

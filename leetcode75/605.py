# Can Place Flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        planted = flowerbed[:]
        for i in range(len(flowerbed)):
            if planted[i] != 1:
                print('i=', i)
                if i > 0 and i < len(flowerbed) - 1:
                    if planted[i + 1] != 1 and planted[i - 1] != 1:
                        planted[i] = 1
                        print('inserted', planted)
                elif i == 0:
                    if (i + 1) > len(flowerbed) - 1:
                        planted[i] = 1
                    elif planted[i + 1] != 1:
                        planted[i] = 1
                        print(planted)
                else:
                    if planted[i - 1] != 1:
                        planted[i] = 1
                        print(planted)
        return sum(planted) - sum(flowerbed) >= n


class Solution2(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        planted = flowerbed[:]
        for i in range(len(flowerbed)):
            if planted[i] != 1:
                left_ok = (i == 0 or planted[i - 1] == 0)
                right_ok = ((i == len(flowerbed) - 1) or planted[i + 1] == 0)

                if left_ok and right_ok:
                    planted[i] = 1

            print(planted)
        return sum(planted) - sum(flowerbed) >= n





flowerbed = [0]
n = 1
testset = Solution2()
print(testset.canPlaceFlowers(flowerbed, n))
flowerbed[1] == 0

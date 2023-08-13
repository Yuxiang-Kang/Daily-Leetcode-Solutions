# Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        dic = {}
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]] = 1
            else:
                dic[arr[i]] += 1
        l = dic.values()
        if len(l)==len(set(l)):
            return True
        return False


arr = [1, 2, 2, 1, 1, 3]
test = Solution()
print(test.uniqueOccurrences(arr))

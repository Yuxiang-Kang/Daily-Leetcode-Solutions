# String Compression
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        k = 0
        for i in range(len(chars)):
            if i == 0 or (chars[i] != chars[i - 1]):
                ms_start = i

            if i == len(chars) - 1 or chars[i] != chars[i + 1]:
                chars[k] = chars[i]
                k += 1

                if i - ms_start > 0:
                    chars[k:k+len(str(i - ms_start + 1))] = [ch for ch in str(i - ms_start + 1)]
                    k += len(str(i - ms_start + 1))
        print(k)
        return chars


chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b",'c','c','a','a','a']
test = Solution()
print(test.compress(chars))

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        while i < len1 or i < len2:
            print(i)
            if i < len1:
                result.append(word1[i])

            if i < len2:
                result.append(word2[i])
            i +=1

        result = "".join(result)

        return result


sol = Solution()
sol.mergeAlternately('abc', 'defg')

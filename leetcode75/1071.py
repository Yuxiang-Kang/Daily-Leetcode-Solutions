# Greatest Common Divisor of Strings
class Solution1(object):
    # Brute method
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        cand = min(str1, str2)
        i = len(cand)
        while i > 0:
            if len(str1) % i == 0:
                if len(str2) % i == 0:
                    print(str1[0:i])
                    if cand[0:i] * int(len(str1) / i) == str1 and cand[0:i] * int(len(str2) / i) == str2:
                        print('get!')
                        print(cand[0:i])
                        return cand[0:i]

            i -= 1
        return "no common divisor"


class Solution2(object):
    # Common divisor method
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 == str2 + str1:
            i = min(len(str1), len(str2))
            while i > 0:
                if len(str1) % i == 0 and len(str2) % i == 0:
                    print(str1[0:i])
                    return str1[0:i]
                i -= 1
        else:
            return ""


sol = Solution2()
sol.gcdOfStrings('abcabcabcabcabcabc', 'abcabcabc')

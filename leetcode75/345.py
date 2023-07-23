# Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        locate = []
        vowel = []
        alfabet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(len(s)):
            print(i)
            if s[i] in alfabet:
                locate.append(i)
                vowel.append(s[i])
        new_s = list(s)
        print(locate)
        print(vowel)
        for i in range(len(locate)):
            new_s[locate[i]] = vowel[len(locate) - 1 - i]
        print(new_s)
        new_s = "".join(new_s)
        print(new_s)
        return new_s


class Solution2(object):
    # 2 pointers
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = list(s)
        i = 0
        j = len(s) - 1
        alfabet = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while 1:
            while new_s[i] not in alfabet and i < len(new_s) - 1:
                i += 1

            while new_s[j] not in alfabet and j > 0:
                j -= 1
            if i >= j:
                break
            print(f"i={i},j={j}")
            m = new_s[i]
            new_s[i] = new_s[j]
            new_s[j] = m
            i += 1
            j -= 1

        new_s = "".join(new_s)
        return new_s


s = "leetcode"
test = Solution2()
print(test.reverseVowels(s))

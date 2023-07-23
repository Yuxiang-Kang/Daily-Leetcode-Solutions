# Reverse Words in a String
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # my thought:get the number and location of each words
        location = []
        length = []
        latest_start = 0
        new_s = []
        print(len(s))
        for i in range(len(s)):
            # print(i)
            word_start = (s[i] != ' ' and (i == 0 or s[i - 1] == ' '))
            word_end = (s[i] != ' ' and (i == len(s) - 1 or s[i + 1] == ' '))
            if word_start:
                location.append(i)
                latest_start = i
            if word_end:
                length.append(i - latest_start + 1)
            # print(f'{word_end},{s[i]}')
        print(f'location:{location}, length:{length}')
        for i in range(len(location) - 1, -1, -1):
            new_s.append(s[location[i]:location[i] + length[i]])
            print(s[location[i]:location[i] + length[i]])
            if i != 0:
                new_s.append(' ')
        new_s = ''.join(new_s)
        print(new_s)
        return new_s


class Solution2(object):
    def reverseWords(self, s):
        # create directly a new list with words
        """
        :type s: str
        :rtype: str
        """
        # my thought:get the number and location of each words
        new_s = []
        print(len(s))
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                latest_start = i
            if s[i] != ' ' and (i == len(s) - 1 or s[i + 1] == ' '):
                new_s.append(s[latest_start:i + 1])
                new_s.append(' ')
        new_s.reverse()
        new_s = "".join(new_s[1:])
        print("".join(new_s[1:]))
        return new_s

class Solution3():
    def reverseWords(self, s):
        # inspired
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])

s = "a good   example"
test = Solution3()
print(test.reverseWords(s))

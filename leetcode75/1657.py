# Determine if Two Strings Are Close
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def word_to_dict(arr):
            dic = {}
            for i in range(len(arr)):
                if arr[i] not in dic:
                    dic[arr[i]] = 1
                else:
                    dic[arr[i]] += 1
            return dic
        dict_1 = word_to_dict(word1)
        dict_2 = word_to_dict(word2)
        print(set(dict_1.keys()))
        print(set(dict_2.keys()))
        if sorted(dict_1.values()) == sorted(dict_2.values()) and set(dict_1.keys())==set(dict_2.keys()):
            return True
        return False

word1 = "uau"
word2 = "ssx"
test=Solution()
print(test.closeStrings(word1,word2))

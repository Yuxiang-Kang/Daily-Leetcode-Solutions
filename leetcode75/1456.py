# Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        judge_list = [0 for _ in range(len(s))]
        print(judge_list)
        for i in range(len(s)):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                judge_list[i] = 1
            else:
                judge_list[i] = 0
        sum_list = [0 for _ in range(len(s) - k + 1)]
        sum_list[0] = sum(judge_list[0:k])
        for i in range(1, len(s) - k + 1):
            sum_list[i] = sum_list[i - 1] - judge_list[i - 1] + judge_list[i + k - 1]
        return max(sum_list)


s = "abciiidef"
k = 3
test = Solution()
print(test.maxVowels(s, k))

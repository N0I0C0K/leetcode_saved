class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)+1
        return word[:i][::-1]+word[i:]


a = Solution()
print(a.reversePrefix('abcde', 'd'))

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        strs = Counter(s)
        res = ''
        for i in range(0, len(s)):
            temp = s[i]
            if strs[temp] == 1:
                res+=temp
            else:
                strs[temp] -= 1
        return res
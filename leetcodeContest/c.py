from typing import *


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dicWords = dict()
        for item in words:
            if item in dicWords:
                dicWords[item] += 1
            else:
                dicWords[item] = 1
        l = 0
        m = 0
        for item in words:
            tword = item[1]+item[0]
            if item[0] != item[1]:
                if (tword) in dicWords and dicWords[(tword)] > 0 and dicWords[item] > 0:
                    l += 4
                    dicWords[tword] -= 1
                    dicWords[item] -= 1
            else:
                if dicWords[item] >= 2:
                    l += 4
                    dicWords[item] -= 2
                elif dicWords[item] == 1:
                    m = 1
        return l + m*2


a = Solution()
print(a.longestPalindrome(['cc', 'cc']))

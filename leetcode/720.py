from typing import *
from functools import cmp_to_key


class Solution:
    def longestWord(self, words: List[str]) -> str:
        w = set(words)

        def cmp(l, r):
            if len(l) != len(r):
                return len(l)-len(r)
            else:
                if l < r:
                    return 1
                elif l > r:
                    return -1
                else:
                    return 0
        words.sort(key=cmp_to_key(cmp), reverse=True)
        for word in words:
            for i in range(1, len(word)):
                if word[:i] not in w:
                    break
            else:
                return word
        return ''


a = Solution()
print(a.longestWord(
    ["b", "aaa", "bb", "aaaa"]))

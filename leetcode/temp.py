# https://leetcode-cn.com/problems/contains-duplicate-ii/

from typing import *


class Solution:
    def countValidWords(self, sentence: str) -> int:
        substr = sentence.split()

        def judge(tar: str) -> bool:
            if not tar.islower() and len(tar) > 1:
                return False
            num0 = ord('0')
            num9 = ord('9')
            numa = ord('a')
            numz = ord('z')
            cnt = 0
            cnt1 = 0
            for i in range((l := len(tar))):
                t = ord(s := tar[i])
                if num0 <= t <= num9:
                    return False
                if s == '!' or s == '.' or s == ',':
                    cnt += 1
                    if l == 1:
                        return True
                    if cnt > 1 or i != l-1:
                        return False
                if s == '-':
                    cnt1 += 1
                    if cnt1 > 1:
                        return False
                    if i == 0 or i == l-1:
                        return False
                    if not (numa <= ord(tar[i-1]) <= numz and numa <= ord(tar[i+1]) <= numz):
                        return False
            return True
        ans: int = 0
        for item in substr:
            if judge(item):
                ans += 1
        return ans


a = Solution()
print(a.countValidWords('a-.'))

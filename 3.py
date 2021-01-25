from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0
        left = 0
        right = 0
        count_s = 1
        max_len = 1
        while right<len_s:
            count_s = right-left+1
            right+=1
            if right == len_s:
                if count_s >= max_len:
                    max_len = count_s
                break
            for i in range(left, right):
                if s[i] == s[right]:
                    left = i+1
                    if count_s>max_len:
                        max_len = count_s
        return max_len

                    


so = Solution()
print(so.lengthOfLongestSubstring("a"))

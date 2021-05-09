
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        tars  = dict()
        len_s = len(s)
        len_t = len(t)
        dn = 1
        for i in range(len_s):
            if s[i] in tars:
                tars[s[i]] += 1
            else:
                tars[s[i]] = 1
        for i in range(len_t):
            if t[i] not in tars:
                return t[i]
            else:
                if tars[t[i]] == 0:
                    return t[i]
                else:
                    tars[t[i]] -= 1

a = Solution()
a.findTheDifference()
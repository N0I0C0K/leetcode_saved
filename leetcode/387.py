class Solution:
    def firstUniqChar(self, s: str) -> int:
        di = dict()
        tar = []
        if s == '':
            return -1
        for i in range(len(s)):
            a = s[i]
            if a in di:
                di[a] += 1
            else:
                di[a] = 1
                tar.append(i)
        for i in tar:
            if di[s[i]] == 1:
                return i
        return -1
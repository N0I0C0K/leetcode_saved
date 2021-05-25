class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        start = 0
        len_1 = 0
        len_0 = 0
        temp = 0
        for i in range(len(s)):
            if s[i] == s[start]:
                temp+=1
            else:
                if s[start] == '1':
                    len_1 = max(len_1, temp)
                else:
                    len_0 = max(len_0, temp)
                start = i
                temp = 1
        if s[start] == '1':
            len_1 = max(len_1, temp)
        else:
            len_0 = max(len_0, temp)
        return len_1>len_0


a = Solution()
print(a.checkZeroOnes('0'))
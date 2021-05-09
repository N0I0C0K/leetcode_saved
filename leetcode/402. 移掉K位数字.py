class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        tar = []
        for i in range(len(num)):
            temp = num[i]
            while k and tar and tar[-1] > temp:
                tar.pop(-1)
                k -= 1
            if temp != '0' or len(tar) != 0:
                tar.append(temp)
        if k > 0:
            tar = tar[:-k]
        if len(tar) == 0:
            return '0'
        return ''.join(tar)
                

a = Solution()
print(a.removeKdigits("10", 1))
# 回溯
# https://leetcode-cn.com/problems/additive-number/

class Solution:
    def check(self, num: str, fir: int, sec: int) -> bool:
        f = int(num[:fir])
        s = int(num[fir:sec])
        tar = f'{f}{s}'
        if len(tar) == len(num):
            return False
        while len(tar) < len(num):
            tar += str(f+s)
            f, s = s, f+s
            if tar != num[:len(tar)]:
                return False
        return tar == num

    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        for fir in range(1, len(num)):
            for sec in range(fir+1, len(num)):
                if self.check(num, fir, sec):
                    return True
        return False


a = Solution()
print(a.isAdditiveNumber("199111992"))

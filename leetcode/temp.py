class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        ans: int = 0
        while num != 0:
            if (num & 1) == 1:
                ans += 1
            num = (num >> 1)
            ans += 1
        return ans-1


a = Solution()
print(a.numberOfSteps(0))

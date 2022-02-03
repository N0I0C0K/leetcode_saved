class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        def dfs(n: int) -> int:
            if n == 0:
                return 0
            if n == 1:
                return 1
            f1, f2 = 1, 1
            while f2 <= n:
                f1, f2 = f2, f1+f2
            return 1+dfs(n-f1)
        return dfs(k)


a = Solution()
print(a.findMinFibonacciNumbers(3))

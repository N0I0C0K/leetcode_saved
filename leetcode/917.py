class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ns = list(s)
        l, r = 0, len(ns)-1
        while l < r:
            while l < r and not ns[l].isalpha():
                l += 1
            while l < r and not ns[r].isalpha():
                r -= 1
            if l == r:
                break
            ns[l], ns[r] = ns[r], ns[l]
            l += 1
            r -= 1
        return ''.join(ns)


a = Solution()
print(a.reverseOnlyLetters('Test1ng-Leet=code-Q!'))

class Solution:
    def maxDepth(self, s: str) -> int:
        sl = list(s)
        tl = []
        max_deep = 0
        deep = 0
        while len(sl) > 0:
            temp = sl.pop(0)
            if temp == '(':
                tl.append(temp)
                deep += 1
                max_deep = max(max_deep, deep)
            elif temp == ')':
                tl.pop()
                deep -= 1
        return max_deep



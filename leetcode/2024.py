class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        prefix = [[0], [0]]
        for i in answerKey:
            if i == 'T':
                prefix[0].append(prefix[0][-1]+1)
                prefix[1].append(prefix[1][-1])
            else:
                prefix[0].append(prefix[0][-1])
                prefix[1].append(prefix[1][-1]+1)

        def check(n: int, c: str = 'T') -> bool:
            nonlocal answerKey, k
            p = 1 if c == 'T' else 0
            for i in range(n, len(answerKey)+1):
                if prefix[p][i]-prefix[p][i-n] <= k:
                    return True
            return False

        lef, rig = 1, len(answerKey)
        while lef < rig:
            mid = (lef+rig+1) >> 1
            if check(mid) or check(mid, 'F'):
                lef = mid
            else:
                rig = mid-1
        return lef


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def maxSize(c: str):
            nonlocal answerKey, k
            ms, lef, sm = 0, 0, 0
            for rig in range(len(answerKey)):
                sm += answerKey[rig] != c
                while sm > k:
                    sm -= answerKey[lef] != c
                    lef += 1
                ms = max(rig-lef+1, ms)
            return ms
        return max(maxSize('T'), maxSize('F'))


a = Solution()
print(a.maxConsecutiveAnswers('TFFT', 1))

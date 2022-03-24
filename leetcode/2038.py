class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        sco = [0, 0]
        cur, cnt = 'C', 0
        for i in colors:
            if cur != i:
                cur = i
                cnt = 1
            else:
                cnt += 1
                if cnt >= 3:
                    sco[ord(cur)-ord('A')] += 1
        return sco[0] > sco[1]


a = Solution()
print(a.winnerOfGame("BBAAABB"))

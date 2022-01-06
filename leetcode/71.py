class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        tar = list(path)
        while len(tar) > 0:
            while len(tar) > 0 and tar[0] == '/':
                tar.pop(0)
            que = ''
            while len(tar) > 0 and tar[0] != '/':
                que += tar.pop(0)
            if que == '.':
                pass
            elif que == '..':
                if len(res) > 0:
                    res.pop()
            else:
                res.append(que)
        tt = ''
        for i in res:
            if i == '':
                continue
            tt += '/'
            tt += i
        return '/' if tt == '' else tt


a = Solution()
print(a.simplifyPath('/../'))

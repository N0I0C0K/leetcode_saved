s = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    res = s[0:k]*(n//k)+s[0:n%k]
    print(res)
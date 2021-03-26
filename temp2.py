n = int(input())
for _ in range(n):
    n, m, idx = map(int, input().split(' '))
    x = idx%n-1
    y = int(idx/n)+1
    ans = x*m+y
    print(f'{ans}')
t = int(input())
for _ in range(t):
    a,b,c,d = map(int, input().split())
    if a!=d:
        print(f'{a} {d}')
    else:
        print(f'{b} {c}')
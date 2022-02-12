a, b = map(int, input().split())
ans = 0
while b != a:
    if b % 2 == 0 and b > a:
        b = b//2
    else:
        b = b+1
    ans += 1
print(ans)

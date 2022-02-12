def check(nums: list, s: int) -> bool:
    t = 0
    for i, item in enumerate(nums):
        t += item
        if t > s:
            return False
        elif t == s:
            t = 0
    return True


def main():
    n = int(input())
    num = list(map(int, input()))
    a = sum(num)
    if a == 0:
        print('YES')
        return
    for k in range(a-1, 0, -1):
        if a % k == 0 and check(num, k):
            print('YES')
            break
    else:
        print('NO')


main()

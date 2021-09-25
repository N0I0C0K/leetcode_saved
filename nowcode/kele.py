
def main():
    n, k, s = map(int, input().split())
    knums = []
    if k > 0:
        knums = list(map(int, input().split()))
    s_b = bin(s)
    s_b = s_b[2:]
    for i in range(len(s_b)-1,-1,-1):
        if s_b[i] == '1' and knums.count(len(s_b)-i) != 0:
            print('NO')
            return
    print('YES')

main()
from collections import Counter


def main():
    n = int(input())
    if n == 0:
        print('no')
        return
    qu = ['1']
    while len(qu) < n:
        t = qu[-1]
        s = ''
        p, num = t[0], 0
        for i in t:
            if i == p:
                num += 1
            else:
                s += f'{num}{p}'
                p = i
                num = 1
        s += f'{num}{p}'
        qu.append(s)
    print(qu[-1])


main()

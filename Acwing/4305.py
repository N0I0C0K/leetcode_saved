

def main():
    res = {}
    nums = 0
    n = int(input())
    for ii in range(n):
        s = input()
        can = False
        id = 0
        for i in s:
            if i in res:
                can = True
                break
        if not can:
            nums += 1
            id = nums
        for i in s:
            res[i] = id
    print(len(set(list(res.values()))))


main()

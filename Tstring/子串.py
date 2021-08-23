def base(n:int, x:int) -> str:
    a=['0','1','2','3','4','5','6','7','8','9','A','b','C','D','E','F']
    b=[]
    while True:
        s=n//x  # 商
        y=n%x  # 余数
        b.append(a[y])
        if s==0:
            break
        n=s
    b.reverse()
    return ''.join(b)

def main():
    t = int(input())
    s = input()
    kmp = None
    for i in range(2,17):
        a = s
        for j in range(1,t+1):
            a = a+base(j,i)
        kmp = [0]*len(a)
        for j in range(1, len(a)):
            k = kmp[j-1]
            while k>0 and a[j] != a[k]:
                k = kmp[k-1]
            if a[j] == a[k]:
                k += 1
            kmp[j] = k
            if k == len(s):
                print('yes')
                return
    print('no')
main()

    

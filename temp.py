def prime(tar):
    res = []
    i = 2
    while i*i <= tar:
        if tar%i == 0:
            while tar%i == 0:
                res.append(i)
                tar = int(tar/i)
        i += 1
    
    res.append(tar)
    return res

while True:
    a = int(input())
    print(prime(a))
def update(tar: list) -> list:
    res = []
    for i in range(len(tar)):
        isT = False
        for j in range(len(tar)):
            if i != j and len(tar[j]) > len(tar[i]) and tar[i] == tar[j][len(tar[j])-len(tar[i]):]:
                isT = True
                break
        if not isT and tar[i] not in res:
            res.append(tar[i])
    return res


user = dict()
nums = int(input())
for i in range(nums):
    info = input().split()
    if info[0] in user:
        user[info[0]] += info[2:]
    else:
        user[info[0]] = info[2:]
    user[info[0]] = update(user[info[0]])
print(len(user.keys()))
for key, item in user.items():
    print(f'{key} {len(item)}', end='')
    for i in item:
        print(f' {i}', end='')
    print('')

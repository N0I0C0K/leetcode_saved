n = int(input())
nums = list(map(int, input().split()))
total = [0]*200
for num in nums:
    total[num%200] += 1
all_ = 0
for num in total:
    all_+=int(num*(num-1)/2)
print(all_)
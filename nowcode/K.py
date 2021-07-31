def get_num(nums:list, k:int):
    minq = []
    maxq = []
    ans = 0
    j = 0
    for i in range(len(nums)):
        while j < len(nums):
            while len(minq) and nums[minq[-1]] >= nums[j]:
                minq.pop()
            minq.append(j)
            while len(maxq) and nums[maxq[-1]] <= nums[j]:
                maxq.pop()
            maxq.append(j)
            if nums[maxq[0]] - nums[minq[0]] > k:
                break
            j += 1
        if minq[0] == i:
            minq.pop(0)
        if maxq[0] == i:
            maxq.pop(0)
        ans+=(len(nums)-j)
    return ans

def getNum(arr, num):
    if arr == None or len(arr) == 0:
        return 0
    qmin = []
    qmax = []
    i = 0
    j = 0
    res = 0
    while i < len(arr):
        while j < len(arr):
            while qmin and arr[qmin[-1]] >= arr[j]:
                qmin.pop()
            qmin.append(j)
            while qmax and arr[qmax[-1]] <= arr[j]:
                qmax.pop()
            qmax.append(j)
            if arr[qmax[0]] - arr[qmin[0]] > num:
                break
            j += 1
        if qmin[0] == i:
            qmin.pop(0)
        if qmax[0] == i:
            qmax.pop(0)
        res += j - i
        i += 1
    len_n = len(nums)
    #print(res)
    res = int((len_n+1)*(len_n)/2)-res
    return res

n,m = list(map(int, input().split()))
nums = list(map(int, input().split()))
for _ in range(m):
    x = int(input())
    print(getNum(nums, x))
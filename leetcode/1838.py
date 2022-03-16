from typing import *


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix = [0]
        a, l = 0, len(nums)
        for num in nums:
            a += num
            prefix.append(a)

        def search(x: int) -> bool:
            nonlocal prefix, nums, k, l
            if x > l:
                return False
            for i in range(x, l+1):
                t = nums[i-1]*x - (prefix[i]-prefix[i-x])
                if t < 0:
                    continue
                if t == 0 or t <= k:
                    return True
            return False

        left, right = 1, l+1
        while left < right:
            mid = (left+right) >> 1
            if search(mid):
                left = mid+1
            else:
                right = mid
        return left-1


a = Solution()
print(a.maxFrequency([9930, 9923, 9983, 9997, 9934, 9952, 9945, 9914, 9985, 9982, 9970, 9932, 9985, 9902, 9975, 9990, 9922, 9990, 9994, 9937, 9996, 9964, 9943, 9963, 9911, 9925, 9935, 9945, 9933, 9916, 9930, 9938, 10000, 9916, 9911, 9959, 9957, 9907, 9913, 9916, 9993, 9930, 9975, 9924, 9988, 9923, 9910, 9925, 9977, 9981, 9927, 9930, 9927, 9925, 9923, 9904, 9928, 9928, 9986, 9903, 9985, 9954, 9938, 9911, 9952, 9974, 9926, 9920, 9972, 9983, 9973, 9917, 9995, 9973, 9977, 9947, 9936, 9975, 9954, 9932, 9964, 9972, 9935, 9946, 9966],
                     3056))

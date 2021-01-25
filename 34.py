from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = self.find(nums, target)
        len_nums = len(nums)
        if result == -1:
            return [-1,-1]
        else:
            right = result
            right_ = True
            left_ = True
            left = result
            copy = nums[result]
            while right<len_nums and left>=0:
                if right+1<len_nums and nums[right+1] == copy:
                    right+=1
                else:
                    right_ = False
                if left-1 >=0 and nums[left-1] == copy:
                    left-=1
                else:
                    left_ = False
                if left_ == False and right_ == False:
                    break
                
            return [left,right]

    def find(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1
        while start<=end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid-1
                continue
            else:
                start = mid+1
                continue
        return -1

So = Solution()
print(So.searchRange([2,2], 2))
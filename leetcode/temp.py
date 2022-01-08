class BinSearch:
    def binSearch(self, nums: list, tar: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left+right) >> 1
            if nums[mid] >= tar:
                right = mid
            else:
                left = mid+1
        return left


so = BinSearch()
print(so.binSearch([1, 2, 4, 4, 5], 7))

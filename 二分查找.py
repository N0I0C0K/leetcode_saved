from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        def b_search_h(tar:int) -> int:
            left, right = 0, n
            while left < right:
                mid = int((left+right)/2)
                if matrix[mid][m-1] == tar:
                    return mid
                elif matrix[mid][m-1] > tar:
                    right = mid
                elif matrix[mid][m-1] < tar:
                    left = mid+1
            
            return left if matrix[n-1][m-1] >= tar else -1
        
        def b_search_w(tar, start, end, h) -> bool:
            if start < 0 or end <0 or start>end:
                return False
            if start == end:
                if matrix[h][start] == tar:
                    return True
                else:
                    return False
            mid = int((start+end)/2)
            if tar > matrix[h][mid]:
                return b_search_w(tar, mid+1, end, h)
            elif tar < matrix[h][mid]:
                return b_search_w(tar, start, mid-1, h)
            else:
                return True

        h = b_search_h(target)
        return b_search_w(target, 0, m-1, h) if h != -1 else False
            
a = Solution()
print(a.searchMatrix([[1]], 10))

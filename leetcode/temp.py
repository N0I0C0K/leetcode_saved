from typing import *


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        lef, rig = 0, len(letters)
        t = ord(target)
        while lef < rig:
            mid = (lef+rig) >> 1
            if ord(letters[mid]) > t:
                rig = mid
            else:
                lef = mid+1
        return letters[rig] if rig < len(letters) else letters[0]


a = Solution()
print(a.nextGreatestLetter(["c", "f", "j"], 'c'))

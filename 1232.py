from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        step_x = coordinates[1][0]-coordinates[0][0]
        step_y = coordinates[1][1]-coordinates[0][1]
        for i in range(1, len(coordinates)):
            temp_x = coordinates[i][0]-coordinates[i-1][0]
            temp_y = coordinates[i][1]-coordinates[i-1][1]
            if temp_x*step_y != step_x*temp_y:
                return False
            step_x = temp_x
            step_y = temp_y
        return True
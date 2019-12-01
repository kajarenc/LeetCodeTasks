def intersaction_length(int_1, int_2):
    intervals = [int_1, int_2]
    intervals.sort()
    
    if intervals[0][1] > intervals[1][0]:
        return 1
    return 0

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_x_projection = [rec1[0], rec1[2]]
        rec1_y_projection = [rec1[1], rec1[3]]
        
        rec2_x_projection = [rec2[0], rec2[2]]
        rec2_y_projection = [rec2[1], rec2[3]]
        
        if intersaction_length(rec1_x_projection, rec2_x_projection) and intersaction_length(rec1_y_projection, rec2_y_projection):
            return True
        return False
        

class Solution:
    """
    Linear solution using two pointer approach
    https://leetcode.com/problems/container-with-most-water/
    """
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) -1

        max_volume = 0
        
        while i < j:
            max_volume = max(max_volume, (j -i) * min(height[i], height[j]))
            
            if height[i] < height[j]:
                i +=1
            else:
                j -=1
            
        return max_volume
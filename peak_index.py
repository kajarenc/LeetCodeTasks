class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        def peakRecursive(l, r, A):
            mid_index = (l + r)  // 2
            left, mid, right = A[mid_index -1], A[mid_index], A[mid_index + 1]
            
            if left < mid and right < mid:
                return mid_index
            elif left < mid < right:
                return peakRecursive(mid_index,r, A)
            elif left > mid > right:
                return peakRecursive(l, mid_index, A)
        return peakRecursive(0, len(A) - 1, A)
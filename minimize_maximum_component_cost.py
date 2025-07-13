from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        self.components -= 1
        return True

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if not edges:
            return 0
        
        # Extract all edge weights for binary search bounds
        weights = [w for u, v, w in edges]
        weights.sort()
        
        left, right = 0, max(weights)
        result = right
        
        def canAchieve(maxCost):
            # Try to form at most k components using edges with weight <= maxCost
            uf = UnionFind(n)
            
            # Only use edges with weight <= maxCost
            for u, v, w in edges:
                if w <= maxCost:
                    uf.union(u, v)
            
            return uf.components <= k
        
        # Binary search on the answer
        while left <= right:
            mid = (left + right) // 2
            if canAchieve(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    n1 = 5
    edges1 = [[0,1,4],[1,2,3],[1,3,2],[3,4,6]]
    k1 = 2
    result1 = solution.minCost(n1, edges1, k1)
    print(f"Example 1: {result1}")  # Expected: 4
    
    # Example 2
    n2 = 4
    edges2 = [[0,1,5],[1,2,5],[2,3,5]]
    k2 = 1
    result2 = solution.minCost(n2, edges2, k2)
    print(f"Example 2: {result2}")  # Expected: 5
    
    # Edge case: no edges
    n3 = 3
    edges3 = []
    k3 = 2
    result3 = solution.minCost(n3, edges3, k3)
    print(f"Edge case (no edges): {result3}")  # Expected: 0
    
    # Edge case: k = n (each node is its own component)
    n4 = 3
    edges4 = [[0,1,10],[1,2,20]]
    k4 = 3
    result4 = solution.minCost(n4, edges4, k4)
    print(f"Edge case (k=n): {result4}")  # Expected: 0
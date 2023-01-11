class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        vertex_degrees = [0] * n
        quick_roads = set()
        for city1, city2 in roads:
            vertex_degrees[city1] += 1
            vertex_degrees[city2] += 1
            quick_roads.add((city1, city2))

        max_total = 0
        for i in range(n):
            for j in range(i+1, n):
                if i == j:
                    continue
                
                total_degrees = vertex_degrees[i] + vertex_degrees[j]
                if (i, j) in quick_roads or (j, i) in quick_roads:
                    total_degrees -= 1
                max_total = max(max_total, total_degrees)
        
        return max_total
        

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i: int = 0
        j: int = -1
        maximum: int = 0
        n: int = len(height)

        while i < n + j:
            if (current := ((n + j) - i) * min(height[i], height[j])) > maximum:
                maximum = current
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return maximum
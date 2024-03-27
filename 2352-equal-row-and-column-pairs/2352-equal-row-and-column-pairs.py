class Solution:
    def equalPairs(self, a: List[List[int]]) -> int:  
        
        rows = Counter(tuple(x) for x in a)
        return sum(rows[tuple(x)] for x in zip(*a))
      
        
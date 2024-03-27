class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        l: int = len(grid)
        d: dict = {}
        for i in range(l):
            t: list = []
            for j in range(l):
                t.append(grid[i][j])
            ts: str = str(t)
            if ts not in d:
                d[ts] = 0
            d[ts] = d[ts] + 1
        
        for i in range(l):
            t: list = []
            for j in range(l):
                t.append(grid[j][i])
            ts: str = str(t)
            if ts not in d:
                d[ts] = 0
            d[ts] = d[ts] + 1
        print(d)
        return sum(list(d.values())) - len(d.values())
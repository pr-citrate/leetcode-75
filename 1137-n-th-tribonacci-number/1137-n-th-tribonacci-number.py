class Solution:
    def tribonacci(self, n: int) -> int:
        if not n: return 0
        if n <= 2: return 1
        t1, t2, t3, trib = 0, 1, 1, 2
        for i in range(2, n):
            trib = t1 + t2 + t3
            t1, t2, t3 = t2, t3, trib
        return trib
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c: Counter = Counter(nums)
        ans: int = 0
        
        for v, n in c.items():
            t: int = k - v
            if v > t & t in c:
                ans += min(n, c[t])
            elif v == t:
                ans += n // 2

        return ans
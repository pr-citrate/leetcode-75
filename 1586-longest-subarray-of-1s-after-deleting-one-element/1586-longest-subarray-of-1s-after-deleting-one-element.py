class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length: int = len(nums)

        lidx: int = 0
        ridx: int = 0
        zeroidx: int = -1
        
        ans: int = 0

        while ridx < length:
            if nums[ridx] == 0:
                ans = max(ans, ridx - lidx - (zeroidx >= lidx))

                lidx = zeroidx + 1
                zeroidx = ridx
            ridx += 1
        else:
            ans = max(ans, ridx - lidx - (zeroidx >= lidx) - (zeroidx < 0))

        return ans
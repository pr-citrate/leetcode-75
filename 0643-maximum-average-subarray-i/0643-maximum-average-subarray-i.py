class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s: int = sum(nums[:k])
        maxs: int = s

        for i in range(len(nums) - k):
            s -= nums[i]
            s += nums[i + k]

            maxs = max(maxs, s)

        return maxs / k
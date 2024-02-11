class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt: int = 0

        for i, num in enumerate(nums):
            if num == 0:
                cnt += 1
            else:
                nums[i - cnt] = num

        if cnt:
            nums[-cnt:] = [0] * cnt
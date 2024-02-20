class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls: int = 0
        rs: int = sum(nums)
        
        for i, n in enumerate(nums):
            rs -= n
            if ls == rs:
                return i
            ls += n
        else:
            return -1
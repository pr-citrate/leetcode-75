class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l: int = len(nums)
        lproducts: list = [1] * l
        rproducts: list = [1] * l

        for i in range(1, l):
            lproducts[i] = lproducts[i - 1] * nums[i - 1]
            rproducts[-(i + 1)] = rproducts[-i] * nums[-i]

        return [lproducts[i] * rproducts[i] for i in range(len(nums))]
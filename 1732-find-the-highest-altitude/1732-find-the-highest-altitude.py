class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt: int = 0
        maxalt: int = 0
        
        for da in gain:
            alt += da
            maxalt = max(maxalt, alt)

        return maxalt
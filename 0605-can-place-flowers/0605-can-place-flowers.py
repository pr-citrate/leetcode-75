class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return n + flowerbed[0] != 2

        cnt: int = 0
        idx: int = 2
        
        if flowerbed[0] + flowerbed[1] == 0:
            cnt += 1
            last_idx = 0
            idx += 1
        
        while idx < len(flowerbed):
            if flowerbed[idx] + flowerbed[idx - 1] + flowerbed[idx - 2] == 0:
                cnt += 1
                idx += 2
            else:
                idx += 1

        if idx == len(flowerbed) and 3 <= len(flowerbed) and flowerbed[-1] + flowerbed[-2] == 0:
            cnt += 1

        return cnt >= n
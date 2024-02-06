class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return n + flowerbed[0] != 2

        cnt: int = 0
        last_idx: int = -1
        idx: int = 2
        if flowerbed[0] + flowerbed[1] == 0:
            cnt += 1
            last_idx = 0
            idx += 1
        
        while idx < len(flowerbed):
            print(idx)
            if flowerbed[idx] + flowerbed[idx - 1] + flowerbed[idx - 2] == 0:
                cnt += 1
                idx += 2
                last_idx: idx
            else:
                idx += 1

        print(idx == len(flowerbed), last_idx < len(flowerbed) - 2, flowerbed[-1] + flowerbed[-2] == 0)

        if idx == len(flowerbed) and last_idx < len(flowerbed) - 2 and flowerbed[-1] + flowerbed[-2] == 0:
            print(idx)
            cnt += 1
        
        print(cnt)
        return cnt >= n
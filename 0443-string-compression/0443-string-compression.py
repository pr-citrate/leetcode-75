class Solution:
    def compress(self, chars: List[str]) -> int:
        widx: int = 0
        ridx: int = 0

        while ridx < len(chars):
            t = ridx
            while t < len(chars) and chars[t] == chars[ridx]:
                t += 1
            
            chars[widx] = chars[ridx]
            widx += 1
            cnt: int = t - ridx
            
            if cnt > 1:
                for c in str(cnt):
                    chars[widx] = c
                    widx += 1
            ridx = t

        return widx

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lidx, ridx = 0, n
        while True:
            m = (lidx + ridx) // 2
            f = guess(m)
            if not f: return m
            if f < 0:
                ridx = m - 1
            else:
                lidx = m + 1
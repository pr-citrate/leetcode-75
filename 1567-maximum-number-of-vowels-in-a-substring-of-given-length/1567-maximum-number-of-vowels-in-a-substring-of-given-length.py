class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels: str= 'aeiouAEIOU'

        idx: int = 0
        w: int = 0

        for c in s[:k]:
            if c in vowels:
                w += 1

        m: int = w

        for i in range(len(s) - k):
            if s[i] in vowels:
                w -= 1
            if s[i + k] in vowels:
                w += 1
            m = max(m, w)

        return m
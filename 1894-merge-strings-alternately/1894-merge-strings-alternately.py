class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        for c in range(min_len):
            ans += word1[c] + word2[c]
        
        longer_str = word1 if len1 >= len2 else word2
        ans += longer_str[min_len:]
        return ans
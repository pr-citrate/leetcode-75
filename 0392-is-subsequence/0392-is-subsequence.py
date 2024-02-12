class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i: int = 0
        if len(s) == 0:
            return True
        for c in t:
            if c == s[i]:
                i += 1
                if i == len(s):
                    return True
        return False
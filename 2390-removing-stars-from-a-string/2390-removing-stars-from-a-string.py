class Solution:
    def removeStars(self, s: str) -> str:
        ans: list[str] = []
        for c in s:
            if c != '*':
                ans.append(c)
            else:
                ans.pop()
        return ''.join(ans)

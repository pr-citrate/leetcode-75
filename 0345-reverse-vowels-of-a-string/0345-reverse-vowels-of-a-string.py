class Solution:
    def reverseVowels(self, s: str) -> str:
        lcnt: int = 0
        rcnt: int = -1
        vowels: str = 'aeiouAEIOU'
        ans: list = list(s)

        while lcnt < len(s) + rcnt:
            match s[lcnt] in vowels, s[rcnt] in vowels:
                case True, True:
                    ans[lcnt], ans[rcnt] = s[rcnt], s[lcnt]
                    lcnt += 1
                    rcnt -= 1
                case False, True:
                    lcnt += 1
                case True, False:
                    rcnt -= 1
                case False, False:
                    lcnt += 1
                    rcnt -= 1
        
        return ''.join(ans)

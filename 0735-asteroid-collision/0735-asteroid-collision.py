class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i: int = 0
        while i < len(asteroids) - 1:
            a: int = asteroids[i]
            b: int = asteroids[i + 1]
            if a > 0 and b < 0:
                if a + b > 0:
                    del asteroids[i + 1]
                elif a + b < 0:
                    del asteroids[i]
                    if i != 0:
                        i -= 1
                else:
                    del asteroids[i + 1]
                    del asteroids[i]
                    if i != 0:
                        i -= 1
            else:
                i += 1
        return asteroids




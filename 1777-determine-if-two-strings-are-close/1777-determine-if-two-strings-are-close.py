class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1: dict = dict(Counter(word1))
        c2: dict = dict(Counter(word2))

        c3: dict = dict(Counter(c1.values()))
        c4: dict = dict(Counter(c2.values()))

        print({*c1.keys()}, {*c2.keys()}, {*c3.keys()}, {*c4.keys()})

        return {*c1.keys()} == {*c2.keys()} and c3 == c4
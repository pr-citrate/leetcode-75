class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c: Counter = Counter(arr)
        v: dict_values = c.values()
        s: set = {*v}
        return len(s) == len(v)
class RecentCounter:

    def __init__(self):
        self.value: int = 0
        self.pings: list[int] = []

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings and self.pings[0] + 3000 < t:
            del self.pings[0]
        return len(self.pings)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
class TimeMap:

    def __init__(self):
        self.kvstore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvstore:
            self.kvstore[key] = []
        self.kvstore[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        output = ''
        valuelist = self.kvstore.get(key, [])
        l, r = 0, len(valuelist) - 1

        while l <= r:
            m = (l + r) // 2
            if valuelist[m][1] <= timestamp:
                output = valuelist[m][0]
                l = m + 1
            else:
                r = m - 1
        return output

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

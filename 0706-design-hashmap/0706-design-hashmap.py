# naive solution with fixed range

MX_SIZE = 10 ** 6 + 1

class MyHashMap:

    def __init__(self):
        self.storage = [None] * MX_SIZE


    def put(self, key: int, value: int) -> None:
        self.storage[key] = value


    def get(self, key: int) -> int:
        return -1 if self.storage[key] is None else self.storage[key]


    def remove(self, key: int) -> None:
        self.put(key, None)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
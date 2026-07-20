from collections import Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique_index = 0
        self.array = []
        self.cnt = Counter()

        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:
        if self.unique_index >= len(self.array):
            return -1

        return self.array[self.unique_index]


    def add(self, value: int) -> None:
        self.array.append(value)
        self.cnt[value] += 1

        while self.unique_index < len(self.array):
            if self.cnt[self.array[self.unique_index]] > 1:
                self.unique_index += 1
            else:
                break


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
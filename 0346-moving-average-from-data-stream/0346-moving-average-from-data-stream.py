class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.count = 0
        self.front = 0
        self.rear = 0

    def push(self, num):
        if self.count == self.size:
            self.pop()

        self.queue[self.front] = num
        self.front = (self.front + 1) % self.size
        self.count += 1

    def pop(self):
        if self.count == 0:
            return

        self.queue[self.rear] = 0
        self.rear = (self.rear + 1) % self.size
        self.count -= 1

    def next(self, val: int) -> float:
        self.push(val)

        return sum(self.queue) / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
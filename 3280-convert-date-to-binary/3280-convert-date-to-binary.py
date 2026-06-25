class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([i[2:] for i in map(lambda t: bin(int(t)), date.split("-"))])

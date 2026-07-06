class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        st = set(sentence)

        for i in range(ord('a'), ord('z') + 1):
            if chr(i) not in st:
                return False

        return True

class Solution:
    def sortSentence(self, s: str) -> str:
        sentence = sorted([(int(i[-1]), i[:-1]) for i in s.split()])
        return " ".join([i[1] for i in sentence])

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        def fill(s, n):
            return s + (n - len(s)) * " "

        n = len(words)
        words = [fill(word, n) for word in words]

        for i in range(n):
            row = words[i]

            col = "".join([words[j][i] for j in range(n)])

            if row != col:
                return False
        
        return True

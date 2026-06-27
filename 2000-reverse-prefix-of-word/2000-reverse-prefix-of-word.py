class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            idx = word.index(ch) + 1

            return word[:idx][::-1] + word[idx:]
        except ValueError:
            return word

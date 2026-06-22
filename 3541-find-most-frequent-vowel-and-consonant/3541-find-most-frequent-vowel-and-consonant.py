from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = Counter({'_': 0})
        consonant = Counter({'_': 0})

        for i in s:
            if i in "aeiou":
                vowel[i] += 1
            else:
                consonant[i] += 1

        return max(vowel.values()) + max(consonant.values())

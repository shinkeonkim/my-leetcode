class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        crt = 0
        ans = 0
    
        for ch in word:
            pos = keyboard.index(ch)
            ans += abs(pos - crt)
            crt = pos
        
        return ans

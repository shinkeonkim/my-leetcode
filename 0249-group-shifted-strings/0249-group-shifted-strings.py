from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        def shift(ch, n):
            k = ord(ch) - ord('a')
            k = (k + n + 26) % 26
            return chr(k + ord('a'))

        def diff(a, b):
            return ord(a) - ord(b)

        def shift_to_a_start(s):
            d = diff('a', s[0])

            return "".join(shift(ch, d) for ch in s)
        
        for s in strings:
            ans[shift_to_a_start(s)].append(s)

        return [i for i in ans.values()]

            
        
from collections import defaultdict

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shift(ch, n):
            k = (ord(ch) - ord('a') + n + 26) % 26
            return chr(k + ord('a'))

        def shift_to_a_start(s):
            d = ord('a') - ord(s[0])
            return "".join(shift(ch, d) for ch in s)

        ans = defaultdict(list)

        for s in strings:
            ans[shift_to_a_start(s)].append(s)

        return [i for i in ans.values()]

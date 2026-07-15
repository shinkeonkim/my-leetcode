from collections import Counter
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_count = Counter()
        last = 0

        char_count[s[last]] += 1
        char_category_count = 1
        ans = 1
        i = 1

        while i < len(s):
            if char_count[s[i]] == 0:
                char_category_count += 1
            char_count[s[i]] += 1

            while char_category_count > 2:
                char_count[s[last]] -= 1
                if char_count[s[last]] == 0:
                    char_category_count -= 1
                last += 1

            if char_category_count <= 2:
                ans = max(ans, i - last + 1)

            i += 1

        return ans

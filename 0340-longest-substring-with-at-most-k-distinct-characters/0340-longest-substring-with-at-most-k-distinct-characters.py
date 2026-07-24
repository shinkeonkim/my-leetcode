from collections import Counter

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        each_counter = Counter()
        categories_count = 0

        start = 0

        each_counter[s[start]] += 1
        categories_count += 1
        ans = 1

        for idx in range(1, len(s)):
            each_counter[s[idx]] += 1
            if each_counter[s[idx]] == 1:
                categories_count += 1

            while categories_count > k and start <= idx:
                each_counter[s[start]] -= 1

                if each_counter[s[start]] == 0:
                    categories_count -= 1
                start += 1

            # print(categories_count, k, start, idx)

            ans = max(ans, idx - start + 1)

        return ans

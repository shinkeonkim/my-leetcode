class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleMap = {'type': 0, 'color': 1, 'name': 2}
        ruleIdx = ruleMap[ruleKey]
        ans = 0

        for item in items:
            if item[ruleIdx] == ruleValue:
                ans += 1

        return ans

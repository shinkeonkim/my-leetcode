from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        def key(s):
            return "".join(sorted(list(s)))
        
        for s in strs:
            groups[key(s)].append(s)
        
        return list(groups.values())
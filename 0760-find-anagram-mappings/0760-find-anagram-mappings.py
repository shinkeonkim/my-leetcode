class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        for i in range(len(nums2)):
            mapping[nums2[i]] = i

        return [mapping[i] for i in nums1]

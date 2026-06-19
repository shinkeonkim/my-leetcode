def is_even_bits_count(num):
    return bin(num).count('1') % 2 == 0

class Solution(object):
    def tripletCount(self, a, b, c):
        """
        :type a: List[int]
        :type b: List[int]
        :type c: List[int]
        :rtype: int
        """
        ans = 0

        for i in a:
            for j in b:
                for k in c:
                    if is_even_bits_count(i ^ j ^ k):
                        ans += 1
        
        return ans
        
        
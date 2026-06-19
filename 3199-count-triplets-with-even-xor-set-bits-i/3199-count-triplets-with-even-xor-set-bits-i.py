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
                    m = i ^ j ^ k
                    if is_even_bits_count(m):
                        ans += 1
        
        return ans
        
        
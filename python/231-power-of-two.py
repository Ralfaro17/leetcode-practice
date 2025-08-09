class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        exponent = 0
        base = 1
        while base <= n:
            if base == n:
                return True
            else:
                exponent += 1
                base = 2 ** exponent
        
        return False

print(Solution().isPowerOfTwo(2 ** 58))

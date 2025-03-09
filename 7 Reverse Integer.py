class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow before updating reversed_num
            if (reversed_num > INT_MAX // 10) or (reversed_num == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            
            reversed_num = reversed_num * 10 + digit
        
        return sign * reversed_num

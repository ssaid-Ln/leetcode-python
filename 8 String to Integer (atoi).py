class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Step 1: Remove leading whitespace
        
        if not s:
            return 0  # If string is empty after removing whitespace
        
        sign = 1  # Step 2: Determine sign
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        result = 0
        while i < len(s) and s[i].isdigit():  # Step 3: Convert digits to integer
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        int_min, int_max = -2**31, 2**31 - 1
        if result < int_min:
            return int_min
        if result > int_max:
            return int_max
        
        return result

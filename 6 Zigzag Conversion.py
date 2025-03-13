class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = ["" for _ in range(numRows)]
        index, step = 0, 1
        
        for char in s:
            rows[index] += char
            
            if index == 0:
                step = 1  # Move down
            elif index == numRows - 1:
                step = -1  # Move up
            
            index += step
        
        return "".join(rows)
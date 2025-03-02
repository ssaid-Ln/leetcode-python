class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num  # Find the number needed to reach target
            
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of the two numbers
            
            num_map[num] = i  
        
        return []  # Should never reach here since the problem guarantees one solution

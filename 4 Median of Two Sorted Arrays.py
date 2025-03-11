class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = sorted(nums1 + nums2)
        
        n = len(merged_array)
        
        if n % 2 == 1:
            return float(merged_array[n // 2])
        else:
            mid1, mid2 = merged_array[n // 2 - 1], merged_array[n // 2]
            return (mid1 + mid2) / 2.0
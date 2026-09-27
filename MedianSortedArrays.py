"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            if i < m:
                left1 = nums1[i]
            else:
                left1 = float('inf')

            if i > 0:
                right1 = nums1[i - 1]
            else:
                right1 = float('-inf')

            if j < n:
                left2 = nums2[j]
            else:
                left2 = float('inf')

            if j > 0:
                right2 = nums2[j - 1]
            else:
                right2 = float('-inf')

            if right1 <= left2 and right2 <= left1:
                if (m + n) % 2 == 1:
                    return float(max(right1, right2))
                else:
                    return (max(right1, right2) + min(left1, left2)) / 2.0

            elif right1 > left2:
                right = i - 1
            else:
                left = i + 1

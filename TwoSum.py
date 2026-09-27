"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice."""

"""
class Solution(object):
    def twoSum(self, nums, target):
        run = 0
        for index in range(len(nums)):
            for index1 in range(index+1,len(nums)):
                if (nums[index] + nums[index1]) == target:
                    a = [index,index1]
                    run = 1
                    return a
                    break
            if run:break
                


        


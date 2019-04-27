class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumps = nums[0] # Jumps is the remaining available jumps
        for i in range(1, len(nums)):
            if jumps == 0:
                return False
            jumps -= 1
            if nums[i] > jumps:
                jumps = nums[i]
        return True

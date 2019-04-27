# 70. Climbing stairs

# Even though this solution yields correct results. it's slow and gets time
# limit exceeded in leetcode.com.
class Solution1(object):
    def climbStairs(self, n):
        """
        Returns the number of ways to climb n steps when you can climb one or
        two each time.
        :type n: int
        :rtype: int
        """
        s = 0
        if n == 0:
            return 1
        if n > 0:
            s = s + self.climbStairs(n - 1)
        if n > 1:
            s = s + self.climbStairs(n - 2)
        return s

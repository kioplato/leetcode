# 70. Climbing stairs

# Even though this solution yields correct results. it's slow and gets time
# limit exceeded in leetcode.com.
class Solution1(object):
    def climbStairs(self, n):
        """
        Returns the number of ways to climb n steps
        when you can climb one or two each time.
        Complexity: O(2^n).
        :type n: int  # The number of stairs to climb.
        :rtype: int  # The number of ways to climb n stairs.
        """
        s = 0
        if n == 0:
            return 1
        if n > 0:
            s = s + self.climbStairs(n - 1)
        if n > 1:
            s = s + self.climbStairs(n - 2)
        return s

# Solution1 calculates results twice because of optimal substructure.
# For example for n = 5 and first step = 1 we calculate for n = 3 the result.
# And again for first step = 2 we calculate the n = 3 result.
# Therefore we can speed up with a table of pre-calculated results.
# This solution earns the Accepted! result on leetcode.com.
class Solution2(object):
    def climbStairs(self, n):
        """
        Returns the number of ways to climb n steps
        when you can climb one or two each time.
        Complexity: O(n).
        :type n: int  # The number of stairs to climb.
        :rtype: int  # The number of ways to climb n stairs.
        """
        memo = [0] * n  # List for memoization.
        return self.climbStairs2(n, memo)
    def climbStairs2(self, n, memo):
        """
        Returns the # of ways to climb n stairs
        while moving 1 or 2 steps each time.
        Complexity: O(n).
        :type n: int  # The number of stairs to climb.
        :rtype: int  # The number of ways to climb n stairs.
        """
        s = 0
        if n == 0:
            return 1
        if n > 0:
            if memo[n - 1 - 1] > 0:
                s = s + memo[n - 1 - 1]
            else:
                rv = self.climbStairs2(n - 1, memo)
                s = s + rv
                memo[n - 1 - 1] = rv
        if n > 1:
            if memo[n - 1 - 2] > 0:
                s = s + memo[n - 1 - 2]
            else:
                rv = self.climbStairs2(n - 2, memo)
                s = s + rv
                memo[n - 1 - 2] = rv
        return s

# After playing around with the problem I noticed the fibonacci sequence
# pattern. Therefore for seeds f_0 = 1 and f_1 = 2 the climbStairs(n) = f_{n-1}.
class Solution3(object):
    def climbStairs(self, n):
        """
        Returns the # of ways to climb n stairs
        while moving 1 or 2 steps each time.
        Time Complexity: O(n).
        Space Complexity: O(1).
        :type n: int  # The number of stairs to climb.
        :rtype: int  # The number of ways to climb n stairs.
        """
        if n < 4:
            return n
        f0 = 1
        f1 = 2
        for cand in range(2, n):  # For f_2 till f_{n-1}.
            rv = f0 + f1
            f0 = f1
            f1 = rv
        return f1

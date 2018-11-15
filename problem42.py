#!/usr/bin/python2.7
# 42. Trapping Rain Water

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Store the number of times each height appears in height list
        # and the number of times each greater height appears
        heights = {}
        for i in range(0, len(height)):
            if height[i] in heights:
                heights[height[i]][0] += 1
                heights[height[i]][2] = i
            else:
                heights[height[i]] = [1, i, i]
        for i,i_value in sorted(heights.iteritems()):
            greater_levels = 0
            first = i_value[1]
            last = i_value[2]
            for j,j_value in heights.iteritems():
                if j > i:
                    greater_levels += j_value[0]
                    if first > j_value[1]:
                        first = j_value[1]
                    if last < j_value[2]:
                        last = j_value[2]
            heights[i][0] += greater_levels 
            heights[i][1] = first
            heights[i][2] = last
        water = 0
        for level in sorted(heights):
            if heights[level][0] > 1:
                first = heights[level][1]
                last = heights[level][2]
                for i in range(first, last + 1):
                    if level > height[i]:
                        water += level - height[i]
                        height[i] = level
            else:
                for i in range(0, len(height)):
                    if level > height[i]:
                        height[i] = level
        return water

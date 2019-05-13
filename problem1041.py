class Solution(object):
    def execute_instructions(self, pos, heading, instructions):
        for order in instructions:
            if order == 'G':
                if heading == 'N':
                    pos = (pos[0] - 1, pos[1])
                elif heading == 'W':
                    pos = (pos[0], pos[1] - 1)
                elif heading == 'E':
                    pos = (pos[0], pos[1] + 1)
                elif heading == 'S':
                    pos = (pos[0] + 1, pos[1])
            elif order == 'L':
                if heading == 'N':
                    heading = 'W'
                elif heading == 'W':
                    heading = 'S'
                elif heading == 'E':
                    heading = 'N'
                elif heading == 'S':
                    heading = 'E'
            elif order == 'R':
                if heading == 'N':
                    heading = 'E'
                elif heading == 'W':
                    heading = 'N'
                elif heading == 'E':
                    heading = 'S'
                elif heading == 'S':
                    heading = 'W'
        return heading, pos
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        heading = 'N'
        pos = (0, 0)
        for testcase in range(0, 4):
            heading, pos = self.execute_instructions(pos, heading, instructions)
            if pos == (0, 0): return True
        return False

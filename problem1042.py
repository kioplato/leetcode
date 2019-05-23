# 1042. Flower Planting With No Adjacent

class Solution(object):
    def smallest_unique(self, neighbors, answer):
        neighbors_flowers = [answer[i - 1] for i in neighbors]
        for i in range(1, 5):
            if i not in neighbors_flowers:
                return i
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        answer = [0 for _ in range(N)]
        graph = [[] for _ in range(N)]
        for x, y in paths:
            graph[x - 1].append(y)
            graph[y - 1].append(x)
        for i in range(N):
            answer[i] = self.smallest_unique(graph[i], answer)
        return answer

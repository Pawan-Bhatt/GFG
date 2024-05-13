
from typing import List
from collections import defaultdict


class Solution:
    def findNumberOfGoodComponent(self, e : int, v : int, edges : List[List[int]]) -> int:
        # code here
        adj = defaultdict(set)
        for fm, to in edges:
            adj[fm].add(to)
            adj[to].add(fm)

        seen = set()
        constituent = defaultdict(set)
        minimum = defaultdict(lambda: float('inf'))

        def fill(root, cur):
            nonlocal adj, seen, constituent
            if cur in seen:
                return
            constituent[root].add(cur)
            minimum[root] = min(minimum[root], len(adj[cur]))
            seen.add(cur)
            for to in adj[cur] - seen:
                fill(root, to)

        for cur in range(1, v + 1):
            fill(cur, cur)

        return sum(1 for root in constituent if minimum[root] == len(constituent[root]) - 1)

#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        e = int(input())

        v = int(input())

        edges = IntMatrix().Input(e, 2)

        obj = Solution()
        res = obj.findNumberOfGoodComponent(e, v, edges)

        print(res)

# } Driver Code Ends
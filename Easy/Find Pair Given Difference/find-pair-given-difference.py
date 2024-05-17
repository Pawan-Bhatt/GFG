
from typing import List


class Solution:

    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        s = set(arr)
        if x == 0 and len(arr) == len(s):

            return -1
        for i in range(n):
            if (arr[i]+x) in s or (arr[i]-x) in s:

                return 1
        return -1
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.findPair(n, x, arr)

        print(res)

# } Driver Code Ends
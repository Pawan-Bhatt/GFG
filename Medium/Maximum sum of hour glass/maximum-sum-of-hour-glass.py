
class Solution:
    def findMaxSum(self, rows, cols, grid):
        if rows < 3 or cols < 3:
            return -1
            
        def gridsum(r, c):
            top_sum = sum(grid[r - 1][c - 1: c + 2])
            middle_sum = grid[r][c]
            bottom_sum = sum(grid[r + 1][c - 1: c + 2])
            return top_sum + middle_sum + bottom_sum
        
        max_sum = float('-inf')
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                subgrid_sum = gridsum(r, c)
                max_sum = max(max_sum, subgrid_sum)
        
        return max_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
      
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N,M=map(int,input().strip().split(" "))
        Mat=[]
        for i in range(N):
            B=list(map(int,input().strip().split(" ")))
            Mat.append(B)
        ob=Solution()
        ans=ob.findMaxSum(N,M,Mat)
        print(ans) 
# } Driver Code Ends
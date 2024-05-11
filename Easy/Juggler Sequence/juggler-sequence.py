#User function Template for python3

import math
class Solution:
    def jugglerSequence(self, n):
        a=[]
        a.append(n)
        for i in range(1,n*10):
            if a[-1]%2!=0 and a[-1]!=1:
                m=math.floor(a[-1]**(3/2))
                a.append(m)
            if a[-1]%2==0and a[-1]!=1:
                m=math.floor(a[-1]**(1/2))
                a.append(m)
        return a

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends
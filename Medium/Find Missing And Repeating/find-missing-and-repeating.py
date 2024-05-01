#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        t = list(set(arr))
        repeated = sum(arr) - sum(t)
        sum1 = (n*(n+1))//2
        missing = sum1 - sum(t)
        return [repeated, missing]
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
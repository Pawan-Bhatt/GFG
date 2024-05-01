#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        if n==0:
            return ''
        if n==1:
            return arr[0]
        
        low = min(arr)
        high = max(arr)
        
        ll = len(low)
        hh = len(high)
        arr.sort()
        ans = ''
        for i in range(min(ll,hh)):
            if arr[0][i]==arr[n-1][i]:
                ans+=arr[0][i]
            else:
                break
        return ans if ans else "-1"
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends
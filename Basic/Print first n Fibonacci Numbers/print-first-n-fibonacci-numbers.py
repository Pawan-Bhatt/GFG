#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        if n<=1:
            return [1]
        ans=[1,1]
        for i in range(2,n):
            ans.append(ans[i-1]+ans[i-2])
        return ans
            
        # your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len(res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends
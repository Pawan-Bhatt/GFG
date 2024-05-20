#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
	    ans = 1
	    while n>0:
	        if n%2==1:
	            ans*=x
	        x*=x
	        x%=m
	        n//=2
	    return ans%m
		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends
#User function Template for python3

class Solution:
    def minSteps(self, d):
        jump, position = 0,0
        while position < d or (position - d)%2 != 0:
            jump += 1
            position += jump
        return jump
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d = int(input())

        ob = Solution()
        print(ob.minSteps(d))

# } Driver Code Ends
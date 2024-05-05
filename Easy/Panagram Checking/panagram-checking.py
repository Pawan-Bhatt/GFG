#User function Template for python3

class Solution:
    
    #Function to check if a string is Pangram or not.
    def checkPangram(self,s):
        dic = [0 for i in range(26)]

        for i in s.lower():
            if i.isalpha():
                dic[ord(i)-ord("a")]+=1
        for i in dic:
            if not i:
                return False
        return True
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        obj = Solution()
        if(obj.checkPangram(s)):
            print(1)
        else:
            print(0)
# } Driver Code Ends
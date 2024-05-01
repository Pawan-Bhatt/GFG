#User function Template for python3

class Solution:
    def reversedBits(self, x):
        # code here 
        # code for int to binary 
        bn = bin(x)[2:]
        # code for binary to 32_bit
        bn_32_bit = bn.zfill(32)
        # print(bn_32_bit)
        # code for reverse an number 
        n_list = list(str(bn_32_bit))
        y = int("".join(n_list[::-1]))
        # code for binary to integer 
        z = int(str(y),2)
        return z

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        X=int(input())
        
        ob = Solution()
        print(ob.reversedBits(X))
# } Driver Code Ends
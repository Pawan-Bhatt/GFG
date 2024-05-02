
class Solution:
    def nthFibonacci(self, n : int) -> int:
        
        fir = 1
        sec = 1
        arr = [fir,sec]
        for i in range(2,n):
            new = (fir+sec)%1000000007
            arr.append(new)
            sec = fir
            fir = new
            # print(arr)
        return arr[-1]
            
            
            
        # code here
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.nthFibonacci(n)
        
        print(res)
        

# } Driver Code Ends
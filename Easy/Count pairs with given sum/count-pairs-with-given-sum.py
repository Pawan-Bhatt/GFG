#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        freq = {}
        count_pairs = 0

        for num in arr:
            # Calculate the complement required to form sum K
            complement = k - num
            # If the complement exists in the hashmap, increment count_pairs
            if complement in freq:
                count += freq[complement]
            # Update the frequency of the current element
            freq[num] = freq.get(num, 0) + 1
    
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
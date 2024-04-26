#User function Template for python3

class Solution:
	def FindExitPoint(self, n, m, matrix):
	 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        curr_dir = 0  # Initial direction: Right
        x, y = 0, 0  # Initial position
    
        while 0 <= x < n and 0 <= y < m:
            if matrix[x][y] == 1:
                matrix[x][y] = 0  # Change 1 to 0
                curr_dir = (curr_dir + 1) % 4  # Turn right
            x += directions[curr_dir][0]
            y += directions[curr_dir][1]
    
        # Exit point
        return [x - directions[curr_dir][0], y - directions[curr_dir][1]]
    		# Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.FindExitPoint(n, m, matrix)
        for _ in ans:
            print(_, end=" ")
        print()

# } Driver Code Ends
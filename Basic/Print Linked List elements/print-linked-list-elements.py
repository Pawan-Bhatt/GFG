#Your task is to complete this function
#Your function should print the data in one line only
#You need not to print new line

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
class Solution:
    def display(self,head):
        temp = head
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        #code here


#{ 
 # Driver Code Starts

class node:
    def __init__(self,x):
        self.data = x
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def insert(self, data):
        if self.head == None:
            self.head = node(data)
            self.tail = self.head
            
        else:
            new_node = node(data)
            self.tail.next = new_node 
            self.tail = new_node
            

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        llist = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            llist.insert(i)
        Solution().display(llist.get_head())
        print('')
 #Contributed by:Harshit Sidhwa
# } Driver Code Ends
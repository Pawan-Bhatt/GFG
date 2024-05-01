#User function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        con = ''
        vov = ''
        temp = head
        while temp:
            if temp.data =="a" or temp.data =="e" or temp.data =="i" or temp.data =="o"or temp.data =="u":
                vov+=temp.data
                temp = temp.next
            else:
                con+=temp.data
                temp = temp.next
        # print(con)
        # print(vov)
        new = vov+con
        
        head1 = Node(new[0])
        hd1 = head1
        for i in new[1:]:
            hd1.next = Node(i)
            hd1 = hd1.next
        return head1
            
            
        # Code here


#{ 
 # Driver Code Starts


# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends
#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

class Solution:
    def findIntersection(self, head1, head2):
        if not head1 or not head2:
            return None  # Handle empty lists
        
        ans_head = None
        ans_tail = None
        temp1 = head1
        temp2 = head2
        
        while temp1 and temp2:
            if temp1.data == temp2.data:
                if ans_head is None:
                    ans_head = Node(temp1.data)
                    ans_tail = ans_head
                else:
                    ans_tail.next = Node(temp1.data)
                    ans_tail = ans_tail.next
                temp1 = temp1.next
                temp2 = temp2.next
            elif temp1.data < temp2.data:
                temp1 = temp1.next
            else:
                temp2 = temp2.next
        
        return ans_head

            
        #return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        ob = Solution()
        result = ob.findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends
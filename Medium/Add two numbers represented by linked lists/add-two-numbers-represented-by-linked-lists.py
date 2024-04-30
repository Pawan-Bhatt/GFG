#User function Template for python3

''' Node for linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, num1, num2):
        ans1 =''
        ans2 = ''
        
        
        
        
        
        
        while num1:
            k = str(num1.data)
            ans1+=k
            num1 = num1.next
            # print(ans1)
        while num2:
            j = str(num2.data)
            ans2+=j
            num2 = num2.next
            # print(ans2)
        new = str(int(ans1)+int(ans2))
        # print(new)
        n = len(new)
        
        head = Node(int(new[0]))
        temp = head
        for i in new[1:]:
            temp.next = Node(int(i))
            temp = temp.next
        return head
            
        # code here
        # return head of sum list


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

# prints the elements of linked list starting with head
def printList(n):
    while n:
        print(n.data,end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        
        n = int(input())
        arr1 = ( int(x) for x in input().split() )
        num1 = LinkedList()
        for i in arr1:
            num1.insert(i)
        
        m = int(input())
        arr2 = ( int(x) for x in input().split() )
        num2 = LinkedList()
        for i in arr2:
            num2.insert(i)
        
        res = Solution().addTwoLists(num1.head, num2.head)
        printList(res)
# } Driver Code Ends
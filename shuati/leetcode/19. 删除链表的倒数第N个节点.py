# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.__head=None
    def is_empty(self):
        if self.__head==None:
            return True
    def travel(self):
        cur=self.__head
        if cur==None:
            return
        while(cur.next!=None):
            print(cur.val, end=' ')
            cur=cur.next

        print(cur.val)

    def add(self, item):
        node=ListNode(item)
        if self.is_empty():
            self.__head=node
        else:
            node.next=self.__head
            self.__head=node
    def f(self):
        return self.__head

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Node = ListNode(None)
        Node.next = head
        first, slow = Node, Node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        return Node.next

        # if head.next == None and n == 1:
        #     head=None
        #     return head
        # first, slow = head, head
        # for i in range(n):
        #     first = first.next
        # while first.next != None:
        #     first = first.next
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head

m=LinkList()
for i in range(1,0,-1):
    m.add(i)
m.travel()
root=m.f()
x = Solution().removeNthFromEnd(root, 1)
m.travel()
print(x)
print(x)
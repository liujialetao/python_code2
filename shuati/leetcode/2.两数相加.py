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
    def append(self, item):
        cur = self.__head
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            while cur:
                pre = cur
                cur = cur.next
            pre.next = node

    def f(self):
        return self.__head
    def ff(self, node):
        self.__head=node

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s%10)
            s //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            p = p.next
            print()

        return dummy.next

m1=LinkList()
m2=LinkList()
for i in [9,9,9,9,9,9,9]:
    m1.append(i)
for i in [9,9,9,9]:
    m2.append(i)
m1.travel()
m2.travel()
root1=m1.f()
root2=m2.f()
x = Solution1().addTwoNumbers(root1, root2)
y = LinkList()
y.ff(x)
y.travel()
print(root1)
print(root2)
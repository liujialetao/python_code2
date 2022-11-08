# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SingleLinkList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        if self.head==None:
            return True
    def append(self, item):
        node = ListNode(item)
        if self.head==None:
            self.head=node
        else:
            cur = self.head
            while (cur.next!=None):
                cur = cur.next
            cur.next = node
    def add(self, item):
        node = ListNode(item)
        node.next=self.head
        self.head = node
    def travel(self):
        cur = self.head
        while (cur!=None):
            print(cur.val, end=' ')
            cur = cur.next
        print('\n')

def f(n1,n2,d=1):
    m1=SingleLinkList()
    for i in range(n1,n2,d):
        m1.append(i)
    return m1
m1=f(1,4)
m2=f(2,8,2)
m1.travel()
m2.travel()


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=p=ListNode()
        while l1 and l2:
            if l1.val<=l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            p.next = ListNode(val)
            p=p.next
        if l1:
            p.next=l1
        else:
            p.next=l2
        return dummy.next

    def mergeTwoLists_digui(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<=l2.val:
            l1.next = self.mergeTwoLists_digui(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_digui(l1, l2.next)
            return l2



k=Solution()
m=k.mergeTwoLists_digui(m1.head, m2.head)
mm = SingleLinkList()
mm.head=m
mm.travel()
mm.travel()
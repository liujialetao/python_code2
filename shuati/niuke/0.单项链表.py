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
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next:
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

    def target(self, k):
        pre = self.head
        while (k - 1):
            pre = pre.next
            k = k - 1
        cur = self.head
        while (pre.next):
            pre = pre.next
            cur = cur.next
        return cur.val


dummy = cur = ListNode(10)
for i in range(4):
    node = ListNode(i)
    cur.next = node
    cur = node
m = SingleLinkList()
for i in range(5):
    m.append(i)
head = m.target(2)
pass
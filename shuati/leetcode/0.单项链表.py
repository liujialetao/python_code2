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

        # cur = self.head
        # while cur:
        #     print(cur.val, end=' ')
        #     # print(cur.val, end= '~')
        #     cur = cur.next

m = SingleLinkList()
for i in range(5,0,-1):
    m.add(i)
m.travel()
m.travel()


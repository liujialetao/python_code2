# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.head = None
    def append(self, item):
        node = ListNode(item)
        if self.head==None:
            self.head=node
        else:
            cur = self.head
            while (cur.next!=None):
                cur = cur.next
            cur.next = node
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
m1=f(1,6)

m1.travel()


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next==None:
            return head
        # if head.next.next==None:
        #     p = head.next
        #     head.next.next = head
        #     head.next=None
        #     return p
        else:
            # p=head.next.next
            # q=head.next
            # head.next.next=head
            # head.next=self.swapPairs(p)
            # return q
            '''以下是标准答案，写法更易懂，利用first_node和second_node做标识，意义明确'''
            first_node = head
            second_node = head.next
            # Swapping
            first_node.next = self.swapPairs(second_node.next)
            second_node.next = first_node
            # Now the head is the second node
            return second_node

    def swapPairs_diedai(self, head: ListNode) -> ListNode:
        if head and head.next:
            pass




k=Solution()
m=k.swapPairs(m1.head)
print(m)
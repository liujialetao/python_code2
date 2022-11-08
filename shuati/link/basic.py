# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        if self.__head == None:
            return True
    def length(self):
        count =0
        cur = self.__head
        while cur:
            count+=1
            cur = cur.next
        return count

    def add(self, item):
        node = ListNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        node = ListNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos<=0:
            self.add(item)
        elif pos>=1 and pos<=self.length():
            node = ListNode(item)
            cur = self.__head
            while pos:
                pre = cur
                cur = cur.next
                pos -= 1
            pre.next = node
            node.next = cur

        else:
            self.append(item)


    def travel(self):
        cur = self.__head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next

    def f(self):
        return self.__head
    def ff(self, node):
        self.__head=node

m = LinkList()
m.append(3)
# m.append(4)
# m.add(2)
# m.add(1)
m.insert(1,1.5)
m.travel()
print()
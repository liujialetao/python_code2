class Node(object):
    '''节点'''

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head == None

    def length(self):
        '''链表长度'''
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        '''链表头部增加元素'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部增加元素'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        # 下面包括了pos=1,只有一个节点的情况  1> 1-1
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            # 指针cur、count指向头结点
            pre = self.__head
            count = 0
            node = Node(item)
            while count < (pos - 1):
                pre = pre.next
                count += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        prev = None  # prev为了操作要删除元素前一个元素的指针，使指针指向下下个元素
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                # 如果item是头结点，prev指向cur
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    prev.next = cur.next
                # 如果找到了要删除的元素，退出循环
                break
            else:
                prev = cur
                cur = cur.next

    def search(self, item):
        '''查找链表中的第一个元素'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    m = SingleLinkList()
    m.insert(0, 0)
    m.insert(2, 2)
    m.insert(1, 1)
    m.travel()

    m.add(2)
    m.add(1)
    m.travel()

    m.append(4)
    m.add(0)
    m.travel()

    m.append(5)
    m.add(-1)
    m.travel()
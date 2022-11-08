class Node:
    def __init__(self, elem, next=None):
        self.elem=elem
        self.next=next

class CycleLinkList:
    def __init__(self):
        self.__head=None
    def is_empty(self):
        if self.__head==None:
            return True
    def travel(self):
        cur=self.__head
        while(cur!=None):
                print(cur.elem, end=' ')
                if cur.next!=self.__head:
                    cur=cur.next
                else:
                    print('\n')
                    break
    def length(self):
        cur=self.__head
        count=0
        while(cur!=None):
            count+=1
            if cur.next!=self.__head:
                cur=cur.next
            else:
                return count
        return count

    def add(self, item):
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=self.__head
        else:
            cur=self.__head
            while(cur.next!=self.__head):
                cur=cur.next
            cur.next=node#将尾节点cur的next指向新的头节点node
            node.next=self.__head
            self.__head=node

    def append(self, item):
        node = Node(item)
        node=Node(item)
        if self.is_empty():
            self.__head=node
            node.next=self.__head
        else:
            cur=self.__head
            while(cur.next!=self.__head):
                cur=cur.next
            cur.next=node#将尾节点cur的next指向新的头节点node
            node.next=self.__head

    def insert(self, pos, item):
        if pos<=0:
            self.add(item)
        elif pos>=self.length():
            self.append(item)
        else:
            pre=self.__head
            count=0
            while(count<pos-1):
                pre=pre.next
                count+=1
            #pre指向了pos的前一个位置    形如：pre-node
            node.next=pre.next
            pre.next=node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            pre = None
            cur = self.__head
            #如果第一个元素就是要remove的
            if cur.elem==item:
                if self.length()==1:
                    self.__head=None
                else:
                #找到尾节点，将尾节点的next(cur.next)指向新的头节点self.__head.next
                    pre=self.__head
                    cur=cur.next
                    while(cur.next!=self.__head):
                        pre=cur
                        cur=cur.next
                    cur.next=self.__head.next
                #self.__head指向新的节点，即原来第二个节点
                    self.__head=self.__head.next
                return
            else:
                #只有一个节点，且不是要找的元素
                if self.length()==1:
                    return
                else:
                    pre=self.__head
                    cur=cur.next
                    while(cur.elem!=item):
                        if cur.next==self.__head:
                            return
                        else:
                            pre=cur
                            cur=cur.next
                    #退出后，找到了cur指向的节点是要删除的
                    pre.next=cur.next

    def search(self, item):
        cur=self.__head
        while(cur!=None):
            if cur.elem==item:
                return True
            else:
                if cur.next!=self.__head:
                    cur=cur.next
                else:
                    return False
        return False

m=CycleLinkList()
m.add(3)
m.add(2)
m.add(1)
m.travel()
m.remove(1)
m.travel()
m.travel()


                



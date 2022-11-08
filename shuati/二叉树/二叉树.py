from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

class Tree:
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = TreeNode(elem)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while(queue):
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def bread_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        ret = []
        while(queue):
            cur_node = queue.pop(0)
            print(cur_node.val, end=' ')
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
    #递归法实现先序遍历
    def xian_order(self, node):
        print(node.val, end=' ')
        if node.left is not None:
            self.xian_order(node.left)
        if node.right is not None:
            self.xian_order(node.right)
    #递归法实现中序遍历
    def zhong_order(self, node):
        if node.left is not None:
            self.zhong_order(node.left)
        print(node.val)
        if node.right is not None:
            self.zhong_order(node.right)
    #递归法实现中序遍历
    def hou_order(self, node):
        if node.left is not None:
            self.hou_order(node.left)
        if node.right is not None:
            self.hou_order(node.right)
        print(node.val)

    #非递归法实现先序遍历
    def xian_order2(self):
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur!=None:
                print(cur.val)
            if cur.right!=None:
                queue.insert(0, cur.right)
            if cur.left!=None:
                queue.insert(0, cur.left)
    def zhong_order2(self, root):
        if root == None:
            return []
        ret = []
        queue = [root]
        while queue:
            if root and root!=1:
                root = root.left
                if root:
                    queue.append(root)
                else:
                    root=1
            else:
                if root==1:
                    cur = queue.pop()
                    ret.append(cur.val)
                    if cur.right:
                        queue.append(cur.right)
                        root = cur.right
        return ret

m=Tree()
for i in range(1,11):
    m.add(i)
print('\n广度优先遍历:')
m.bread_travel()
# print('\n先序遍历:')
# m.xian_order(m.root)
# print('\n先序遍历2:')
# m.xian_order2()
# print('\n中序遍历:')
# m.zhong_order(m.root)

# print('\n中序遍历2:')
# ret = m.zhong_order2(m.root)
# print('\n中序遍历:')
# m.zhong_order(m.root)
# print('\n后序遍历:')
# m.hou_order(m.root)


pass





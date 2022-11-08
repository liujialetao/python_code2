# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        while(queue):
            cur_node = queue.pop(0)
            print(cur_node.val)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

class Solution:
    def miDepth(self, root: TreeNode) -> int:
        count=0
        cur=[root]
        if root!=None:
            count=1
        else:
            return 0
        while cur:
            next_layer_node=[]
            for node in cur:
                next_layer_node.append(node.left)
                next_layer_node.append(node.right)
            if None not in next_layer_node:
                cur=next_layer_node
                count+=1
            else:
                return count

    def maxDepth(self, root: TreeNode) -> int:
        count=0
        cur=[root]
        if root!=None:
            count=1
        else:
            return 0
        while cur:
            next_layer_node=[]
            for node in cur:
                next_layer_node.append(node.left)
                next_layer_node.append(node.right)
            flag=0
            for i in next_layer_node:
                if i != None:
                    flag+=1
            if flag>1:
                count+=1
                cur =
            else


m=Tree()
for i in range(1,3):
    m.add(i)
m.bread_travel()
count = Solution().minDepth(m.root)
print('count:',count)
m.bread_travel()


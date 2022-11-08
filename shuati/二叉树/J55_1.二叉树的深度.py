from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self):
        self.root = None
    def add(self, item):
        node = TreeNode(item)
        if self.root==None:
            self.root=node
            return
        queue=[self.root]
        while queue:
            cur=queue.pop(0)
            if cur.left==None:
                cur.left=node
                return
            else:
                queue.append(cur.left)
            if cur.right==None:
                cur.right=node
                return
            else:
                queue.append(cur.right)
    def breath_travle(self):
        if self.root==None:
            return
        queue = [self.root]
        while queue:
            cur=queue.pop(0)
            print(cur.val, end=' ')
            if cur.left!=None:
                queue.append(cur.left)
            if cur.right!=None:
                queue.append(cur.right)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        queue = [root]
        next_queue = []
        if root:
            n = 1
        else:
            return 0
        while True:
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            if queue!=[]:
                n+=1
            else:
                break
        return n

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return max(self.maxDepth2(root.left), self.maxDepth2(root.right)) + 1



m=Tree()
for i in range(1,6):
    m.add(i)
# m.root.left.left=None
# m.root.left.right=None



x=Solution().maxDepth(m.root)
x2=Solution().maxDepth2(m.root)
print(x)
print(x)








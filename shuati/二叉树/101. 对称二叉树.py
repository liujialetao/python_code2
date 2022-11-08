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
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if left and right:
                if left.val == right.val:
                    return dfs(left.left, right.right) and dfs(left.right, right.left)
                else:
                    return False
            if left or right:
                return False
            if left == None and right == None:
                return True

        if root == None:
            return True
        else:
            return dfs(root.left, root.right)

m1=Tree()
m1.add(1)
m1.add(2)
m1.add(2)
m1.add(3)
m1.add(4)
m1.add(4)
m1.add(3)
m1.root.left.right=None
m1.root.right.left=None


x=Solution().isSymmetric(m1.root)
print(x)
print(x)








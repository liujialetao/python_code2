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
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        ret, stack = [], [root]
        while stack:
            root = stack[0]
            if root:
                if root.left==None and root.right==None:
                    ret.append(root.val)
                    stack.pop(0)
                else:
                    if root.right:
                        stack.insert(0, root.right)
                        root.right=None
                    if root.left:
                        stack.insert(0, root.left)
                        root.left=None
        return ret

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res

    def postorderTraversal4(self, root: TreeNode) -> List[int]:
        if not root:
            return list()

        res = list()
        stack = list()
        prev = None

        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if not root.right or root.right == prev:
                    res.append(root.val)
                    prev = root
                    root = None
                else:
                    stack.append(root)
                    root = root.right
        return res

m = Tree()
for i in range(1, 11):
    m.add(i)
solution = Solution()

res2=solution.postorderTraversal4(m.root)
res3=solution.postorderTraversal3(m.root)
res1=solution.postorderTraversal1(m.root)
pass
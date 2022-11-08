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


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def f(root):
            if root==None:
                return True
            if root.val == 0 and root.left == None and root.right == None:
                return True
            else:
                return False

        def dfs(root):
                if f(root.left):
                    root.left = None
                else:
                    dfs(root.left)

                if f(root.right):
                    root.right = None
                else:
                    dfs(root.right)
                return root

        def maxDepth(root: TreeNode) -> int:
            if not root:
                return 0
            else:
                return max(maxDepth(root.left), maxDepth(root.right)) + 1
        n=maxDepth(root)
        for i in range(n):
            if maxDepth(root)==1:
                if root.val == 0 and root.left == None and root.right == None:
                    root=None
                return root
            else:
                root = dfs(root)
        return root
m=Tree()
m.add(1)
m.root.right=TreeNode(0)
m.root.right.left=TreeNode(0)
m.root.right.right=TreeNode(1)
# m.root.left = TreeNode(0)
# m.root.left.left = TreeNode(0)
# m.root.left.right = TreeNode(0)
#
# m.root.right = TreeNode(1)
# m.root.right.left = TreeNode(0)
# m.root.right.right = TreeNode(1)


print('\n广度优先遍历:')
m.bread_travel()

x = Solution().pruneTree(m.root)
pass





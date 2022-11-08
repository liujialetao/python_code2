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
    def isBalanced(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced2(self, root: TreeNode) -> bool:
        def maxDepth(root: TreeNode) -> int:
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
                if queue != []:
                    n += 1
                else:
                    break
            return n
        if not root:
            return True
        return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and self.isBalanced2(root.left) and self.isBalanced2(root.right)

    def isBalanced3(self, root: TreeNode) -> bool:
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
m=Tree()
for i in range(1,10):
    m.add(i)
m.root.right.left=None
m.root.right.right=None

res = Solution().isBalanced2(m.root)
pass
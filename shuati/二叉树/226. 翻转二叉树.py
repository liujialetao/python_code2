# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree(object):
    def __init__(self,root=None):
        self.root = root
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
    def preorder(self, node):
        if node!=None:
            print(node.val, end=' ')
        if node.left!=None:
            self.preorder(node.left)
        if node.right!=None:
            self.preorder(node.right)
def creat_TreeNode(n1,n2,d=1):
    m1 = Tree()
    for i in range(n1, n2, d):
        m1.add(i)
    return m1
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
           return
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root




    def invertTree1(self, root: TreeNode) -> TreeNode:
        return None if root==None else TreeNode(root.val, self.invertTree1(root.right), self.invertTree1(root.left))

    def invertTree2(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                temp = node.left
                node.left = node.right
                node.right = temp
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root
m1=creat_TreeNode(1,9)
m1.breath_travle()

print('\n')
m1.preorder(m1.root)


m2=Solution().invertTree(m1.root)

k2=Tree(m2)
print('\nk2:')
k2.breath_travle()
k2.breath_travle()
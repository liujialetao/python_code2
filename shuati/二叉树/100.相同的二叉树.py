from BaseTree import TreeNode, Tree

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # p和q都是非空，再比较p.val、q.val
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        # p、q有一个为None，返回False
        if p or q:
            return False
        # p、q都为空，返回True
        if p==None and q==None:
            return True


m1=Tree()
m2=Tree()
for i in range(1, 5):
    m1.add(i)
    m2.add(i)
x = Solution().isSameTree(m1.root, m2.root)
pass








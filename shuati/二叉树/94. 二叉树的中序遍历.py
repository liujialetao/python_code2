from BaseTree import TreeNode,Tree
from typing import List



class Solution:
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        def dfs(cur):
            if not cur:
                return
            # 前序递归
            dfs(cur.left)
            res.append(cur.val)
            dfs(cur.right)
        res = []
        dfs(root)
        return res

    def inorderTraversal3(self, root: TreeNode) -> List[int]:
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

    def inorderTraversal3_1(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        ret = []
        queue = [root]
        while queue:
            if root:
                root = root.left
                if root:
                    queue.append(root)
            else:
                cur = queue.pop()
                ret.append(cur.val)
                if cur.right:
                    queue.append(cur.right)
                    root = cur.right
        return ret

    def inorderTraversal4(self, root: TreeNode) -> List[int]:
        ret, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temNode = stack.pop()
                ret.append(temNode.val)
                root = temNode.right
        return ret

    #借鉴后序遍历的方法
    def inorderTraversal5(self, root: TreeNode) -> List[int]:
        ret, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            temNode = stack.pop()
            ret.append(temNode.val)
            root = temNode.right
        return ret
m = Tree()
for i in range(1, 11):
    m.add(i)
solution = Solution()
res1=solution.inorderTraversal1(m.root)
res2=solution.inorderTraversal2(m.root)
res3=solution.inorderTraversal3_1(m.root)
res4=solution.inorderTraversal4(m.root)

print(res)
print(res)

#!/usr/bin/env python
# coding=utf-8

from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)
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
        queue = [self.root]
        while(queue):
            cur_node = queue.pop(0)
            if cur_node!=None:
                print(cur_node.val)
            if cur_node.left!=None:
                queue.append(cur_node.left)
            if cur_node.right!=None:
                queue.append(cur_node.right)
    #递归算法
    def preoder_travel(self, root):
        if root.left!=None:
            self.preoder_travel(root.left)
        print(root.val)
        if root.right!=None:
            self.preoder_travel(root.right)
    #非递归法
    def xianxu_travel(self):
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur!=None:
                print(cur.val)
            if cur.right!=None:
                queue.insert(0, cur.right)
            if cur.left!=None:
                queue.insert(0, cur.left)
    #
m = TreeNode()
for i in range(1,7):
    m.add(i)
m.bread_travel()
print('先序遍历')
# m.preoder_travel(m.root)
m.xianxu_travel()
pass


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        val_list = []
        node_list = [root]
        while(node_list):
            single_val_list = []
            single_node_list = []
            for node in node_list:
                single_val_list.append(node.val)
                if node.left!=None:
                    single_node_list.append(node.left)
                if node.right!=None:
                    single_node_list.append(node.right)
            val_list.append(single_val_list)
            node_list.append(single_node_list)
            node_list=single_node_list
        return val_list




# class Solution3(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         import collections
#         queue = collections.deque()
#         queue.append(root)
#         res = []
#         while queue:
#             size = len(queue)
#             level = []
#             for _ in range(size):
#                 cur = queue.popleft()
#                 if not cur:
#                     continue
#                 level.append(cur.val)
#                 queue.append(cur.left)
#                 queue.append(cur.right)
#             if level:
#                 res.append(level)
#         return res
#








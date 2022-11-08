# -*- coding: utf-8 -*-
# @Time    : 2022/11/4 17:49
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


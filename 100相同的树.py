
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        #如果两个二叉树都为空，则两个二叉树相同。
        if not p and not q:
            return True
        #如果两个二叉树都不为空，那么首先判断它们的根节点的值是否相同， 
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        #递归地判断两个二叉树是否相同。
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
#深度优先搜索

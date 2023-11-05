from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        res2=[]
        for i in res:
            res2.append(i)

        a=len(res)
        res3=[]
        print(res2)
        while a>0:
            res3.append(res.pop())
            a=a-1
        print(res3)
        if res2==res3:
            return True

        else:
            return False
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(2)
#root.left.right=TreeNode(4)
root.right.left=TreeNode(2)
#root.right.right=TreeNode(3)
solution = Solution()
solution.isSymmetric(root)

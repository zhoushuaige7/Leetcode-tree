from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if not root:
            return []
        res=[]
        queue = deque()
        queue.append(root)
        while queue:
            tmp=[]
            length=len(queue)   #找出该层共有几个节点数量        
            for i in range(length):
                node = queue.popleft()#从左边推出该节点，并判断是否含有子节点
                tmp.append(node.val)#加入tem数组，为了实现[[],[]]的输出形式
                if node.left:#若有，则添加到队列末端
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)#完成一组循环代表把该层的节点全部添加进res，并把所以子节点添加进队列
        return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print(solution.levelOrder(root))

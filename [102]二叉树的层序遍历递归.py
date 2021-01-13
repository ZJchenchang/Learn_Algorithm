# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 
#  👍 743 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # if not root:
        #     return []
        # res = []
        # deque = [root]
        # while deque:
        #     size = len(deque)
        #     cur = []
        #     for i in range(size):
        #         r = deque.pop(0)
        #         cur.append(r.val)
        #         if r.left:
        #             deque.append(r.left)
        #         if r.right:
        #             deque.append(r.right)
        #     res.append(cur)
        # return res

        if not root:
            return []
        res = []
        def dfs(index, r:TreeNode):
            if len(res) < index + 1:
                res.append([])
            res[index].append(r.val)
            if r.left:
                dfs(index + 1, r.left)
            if r.right:
                dfs(index + 1, r.right)
        dfs(0, root)
        return res







# leetcode submit region end(Prohibit modification and deletion)

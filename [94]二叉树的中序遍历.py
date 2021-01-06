# 给定一个二叉树的根节点 root ，返回它的 中序 遍历。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：root = [1]
# 输出：[1]
#  
# 
#  示例 4： 
# 
#  
# 输入：root = [1,2]
# 输出：[2,1]
#  
# 
#  示例 5： 
# 
#  
# 输入：root = [1,null,2]
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数目在范围 [0, 100] 内 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 814 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 我困惑程序如何识别输入的节点性质是左还是右。Q1:比如【1,2,3，null，4,5】4如果视作3的右节子，那5到底是4的左节子？还是往上的3的右节子？
        # Q2:如果不输入null，是否一直视为无限的左节子延伸。【1,2,3,4】就是一个只有左子树的树。在类的构造函数中，没有指定left的使用，如何就自动拥有# 了left节点呢?
        res = []
        stack = []
        cur = root
        # 中序，模板：先用指针找到每颗子树的最左下角，然后进行进出栈操作
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res



        
# leetcode submit region end(Prohibit modification and deletion)

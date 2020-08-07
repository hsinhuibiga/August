#Vertical Order Traversal of a Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.m_ = list()
        self.dfs(root, 0, 0)
        self.m_.sort()
        res = [[self.m_[0][2]]]
        for i in range(1, len(self.m_)):
            if self.m_[i][0] == self.m_[i - 1][0]:
                res[-1].append(self.m_[i][2])
            else:
                res.append([self.m_[i][2]])
        return res

    def dfs(self, root, x, y):
        if not root: return
        self.m_.append((x, -y, root.val))
        self.dfs(root.left, x - 1, y - 1)
        self.dfs(root.right, x + 1, y - 1)
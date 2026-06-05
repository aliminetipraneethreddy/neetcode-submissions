# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                result.append(None)

            result.append(node.val)  # Root
            dfs(node.left)           # Left
            dfs(node.right)          # Right

        dfs(root)
        return result
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a1=self.preorderTraversal(p)
        a2=self.preorderTraversal(q)
        k=True
        print(a1)
        print(a2)
        return True
        if len(a1)==len(a2):
            for i in range(len(a1)):
                if a1[i]==a2[i]:
                    k=True
                    continue
                else:
                    return False
        else:
            return False
        if k==True:
            return True



        
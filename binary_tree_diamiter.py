# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def read_way(self, root: Optional[TreeNode]):
    node = root
    while 1:
        print(f"{node.val}")
        if node.left:
            node = node.left
        else:
            break


class Solution:
    max_way_length = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        print(root)
        Solution.node_processing(root)
        return Solution.max_way_length

    # Return (longest_way, longest_branch).
    # longest_way = length of the longest path throw this node.
    # longest_branch = length of the longest patch from this node to some further sheet.

    def node_processing(node: TreeNode) -> (int, int):
        l_w_l, l_b_l, l_w_r, l_b_r = 0, 0, 0, 0
        if not node.left and not node.right:
            print(node.val, "->", 0, 0)
            return 0, 0
        if node.left:
            l_w_l, l_b_l = Solution.node_processing(node.left)
        if node.right:
            l_w_r, l_b_r = Solution.node_processing(node.right)
        longest_way = ((l_b_l + 1) if node.left else 0) + ((l_b_r + 1) if node.right else 0)
        print("longest_way", longest_way)
        print("Solution.max_way_length", Solution.max_way_length)
        Solution.max_way_length = max(Solution.max_way_length, longest_way)
        longest_branch = max(l_b_l, l_b_r) + 1
        print(node.val, "->", longest_way, longest_branch)
        return longest_way, longest_branch

    def diameterOfBinaryTree_1(self, root: Optional[TreeNode]) -> int:
        maxD = [0]
        self.maxDhelper(maxD, root)
        return maxD[0]

    def maxDhelper(self, maxD, node):
        if node == None: return 0

        leftD = self.maxDhelper(maxD, node.left)
        rightD = self.maxDhelper(maxD, node.right)

        maxD[0] = max(maxD[0], leftD + rightD)
        return max(leftD, rightD) + 1

    def diameterOfBinaryTree_2(self, root: Optional[TreeNode]) -> int:
        max_d = 0

        def seek(node: TreeNode) -> int:
            if not node:
                return -1
            if not node.left and not node.right:
                return 0
            l_d, r_d = seek(node.left), seek(node.right)
            max_dist_to_sheet = max(l_d, r_d) + 1
            print(node.val, "->", max_dist_to_sheet)
            nonlocal max_d
            max_d = max(max_d, l_d + r_d + 2)
            return max_dist_to_sheet
        seek(root)
        return max_d



n8 = TreeNode(8, None, None)
n6 = TreeNode(6, None, None)
n7 = TreeNode(7, n8, None)
n5 = TreeNode(5, n6, n7)
n4 = TreeNode(4, None, None)
n2 = TreeNode(2, n4, n5)
n3 = TreeNode(3, None, None)
n1 = TreeNode(1, n2, n3)

a2 = TreeNode(1, None, None)
a1 = TreeNode(1, a2, None)



print(Solution.diameterOfBinaryTree_2(None, n1))

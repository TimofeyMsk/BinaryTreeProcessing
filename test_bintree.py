from unittest import TestCase
from bintree import TreeNode, BinaryTree


class TestBinTreeProcessing(TestCase):
    n9 = TreeNode(9, None, None)  # 3 line
    n8 = TreeNode(8, None, None)  # 5 line
    n6 = TreeNode(6, None, None)  # 4 line
    n7 = TreeNode(7, n8, None) # 4 line
    n5 = TreeNode(5, n6, n7)  # 3 line
    n4 = TreeNode(4, None, None)  # 3 line
    n3 = TreeNode(3, None, n9)  # 2 line
    n2 = TreeNode(2, n4, n5)  # 2 line
    n1 = TreeNode(1, n2, n3)  # 1 line,  good big tree
    n1_array = [1] + [2, 3] + [4, 5, None, 9] + [None, None, 6, 7, None, None, None, None]
    n1_array += [None, None,None, None,None, None, 8, None, None, None,None, None, None, None, None, None]

    m8 = TreeNode(8, None, None)
    m6 = TreeNode(6, None, None)
    m7 = TreeNode(7, m8, None)
    m5 = TreeNode(5, m6, m7)
    m4 = TreeNode(4, None, None)
    m2 = TreeNode(None, m4, m5)  # corrupted node.val
    m3 = TreeNode(3, None, None)
    m1 = TreeNode(1, m2, m3)

    tree_with_type_trash = TreeNode(0, TreeNode(1), 3)

    def test_to_array(self):
        self.assertRaises(TypeError, BinaryTree.to_array_view, 3)
        self.assertRaises(TypeError, BinaryTree.to_array_view, [])
        self.assertRaises(TypeError, BinaryTree.to_array_view, self.tree_with_type_trash)
        self.assertRaises(ValueError, BinaryTree.to_array_view, self.m1)
        self.assertEqual(BinaryTree.to_array_view(self.n1), self.n1_array,
                         'Incorrect convert tree (TreeNode) to array.')

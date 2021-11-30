from unittest import TestCase
from BinaryTree import TreeNode, BinaryTree


class TestBinTreeProcessing(TestCase):
    n9 = TreeNode(9, None, None)  # 3 line
    n8 = TreeNode(8, None, None)  # 5 line
    n7 = TreeNode(7, n8, None)  # 4 line
    n6 = TreeNode(6, None, None)  # 4 line
    n5 = TreeNode(5, n6, n7)  # 3 line
    n4 = TreeNode(4, None, None)  # 3 line
    n3 = TreeNode(3, None, n9)  # 2 line
    n2 = TreeNode(2, n4, n5)  # 2 line
    n1 = TreeNode(1, n2, n3)  # 1 line,  good big tree
    n1_levels = [[1], [2, 3], [4, 5, None, 9], [None, None, 6, 7, None, None, None, None],
                 [None, None, None, None, None, None, 8, None, None,
                  None, None, None, None, None, None, None]
                 ]
    n1_array = [1] + [2, 3] + [4, 5, None, 9] + [None, None, 6, 7, None, None, None, None]
    n1_array += [None, None, None, None, None, None, 8, None, None,
                 None, None, None, None, None, None, None]

    m8 = TreeNode(8, None, None)
    m6 = TreeNode(6, None, None)
    m7 = TreeNode(7, m8, None)
    m5 = TreeNode(5, m6, m7)
    m4 = TreeNode(4, None, None)
    m2 = TreeNode(None, m4, m5)  # corrupted node.val
    m3 = TreeNode(3, None, None)
    m1 = TreeNode(1, m2, m3)

    tree_with_type_trash = TreeNode(0, TreeNode(1), 3)

    def test_to_array_view(self):
        self.assertRaises(TypeError, BinaryTree.__to_array_view__, 3)
        self.assertRaises(TypeError, BinaryTree.__to_array_view__, [])
        self.assertRaises(TypeError, BinaryTree.__to_array_view__, self.tree_with_type_trash)
        self.assertRaises(ValueError, BinaryTree.__to_array_view__, self.m1)
        self.assertEqual(BinaryTree.__to_array_view__(self.n1), self.n1_array,
                         'Incorrect convert tree (TreeNode) to array.')

    def test_to_tree_node_view(self):
        # n1_generated = BinaryTree.__to_tree_node_view__(self.n1_array)
        n1_bt_generated = BinaryTree(self.n1_array)
        n1_array_generated = BinaryTree.__to_array_view__(n1_bt_generated.get_root())
        self.assertEqual(self.n1_array, n1_array_generated,
                         "Incorrect convert from array view to tree_node view.")

    def test_diameter(self):
        self.assertEqual(6, BinaryTree(self.n1).diameter())
        self.assertEqual(0, BinaryTree(TreeNode(0)).diameter())
        self.assertEqual(1, BinaryTree(TreeNode(0, None, TreeNode(1))).diameter())

    def test_depth(self):
        self.assertEqual(5, BinaryTree(self.n1).height())
        self.assertEqual(1, BinaryTree(TreeNode(0)).height())
        self.assertEqual(2, BinaryTree(TreeNode(0, None, TreeNode(1))).height())
        self.assertEqual(3, BinaryTree([3, 9, 20, None, None, 15, 7]).height())

    def test_is_height_balanced(self):
        self.assertEqual(True, BinaryTree([0]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0, 1, None]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0, None, 2]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0, 1, 2]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0] + [1, 2] + [3, None, 4, 5]).is_height_balanced())
        self.assertEqual(True, BinaryTree([3, 9, 20, None, None, 15, 7]).is_height_balanced())
        #self.assertEqual(False, BinaryTree([1, 2, 2, 3, 3, None, None, 4, 4, None, None, None, None]).is_height_balanced())

    def test_to_levels(self):
        self.assertEqual(self.n1_levels, BinaryTree(self.n1).to_levels())
        self.assertEqual([[0], [1, 2], [3, None, 4, 5]],
                         BinaryTree([0] + [1, 2] + [3, None, 4, 5]).to_levels())

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
    n1_levels = [[1], [2, 3], [4, 5, None, 9],
                 [None, None, 6, 7, None, None, None, None],
                 [None, None, None, None, None, None, 8, None, None,
                  None, None, None, None, None, None, None]
                 ]
    n1_array_with_none_tail = [1] + [2, 3] + [4, 5, None, 9] + \
                              [None, None, 6, 7, None, None, None, None] + \
                              [None, None, None, None, None, None, 8, None,
                               None,
                               None, None, None, None, None, None, None]
    n1_array_no_tail = [1] + [2, 3] + [4, 5, None, 9] + \
                       [None, None, 6, 7, None, None, None, None] + \
                       [None, None, None, None, None, None, 8]

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
        self.assertRaises(TypeError, BinaryTree.__to_array_view__,
                          self.tree_with_type_trash)
        self.assertRaises(ValueError, BinaryTree.__to_array_view__, self.m1)
        self.assertEqual(BinaryTree(self.n1).to_array_view(True),
                         self.n1_array_with_none_tail,
                         'Incorrect convert tree (TreeNode) to array.')
        self.assertEqual(BinaryTree(self.n1).to_array_view(False),
                         self.n1_array_no_tail,
                         'Incorrect convert tree (TreeNode) to array.')

    def test_to_tree_node_view(self):
        n1_bt_generated = BinaryTree(self.n1_array_with_none_tail)
        n1_array_generated = \
            BinaryTree.__to_array_view__(n1_bt_generated.get_root(),
                                         add_none_tail=True)
        self.assertEqual(self.n1_array_with_none_tail, n1_array_generated,
                         "Incorrect convert from array view to tree_node view.")

    def test_init(self):
        self.assertEqual(self.n1_array_with_none_tail,
                         BinaryTree(self.n1).to_array_view(add_none_tail=True))
        self.assertEqual(self.n1_array_with_none_tail,
                         BinaryTree(self.n1_array_with_none_tail)
                         .to_array_view(
                             add_none_tail=True))
        self.assertEqual([0] + [1, 2] + [3, None, None, None] +
                         [4, None, None, None, None, None, None, None],
                         BinaryTree([0] + [1, 2] + [3, None, None, None] + [4])
                         .to_array_view(add_none_tail=True))
        self.assertEqual([0] + [1, 2] + [3, None, None, None] + [None, 4],
                         BinaryTree([0] + [1, 2] + [3, None, None, None] +
                                    [None, 4, None]).to_array_view())
        self.assertRaises(ValueError, BinaryTree, [])
        self.assertRaises(TypeError, BinaryTree, -1)
        # noinspection PyTypeChecker
        self.assertRaises(ValueError, BinaryTree,
                          [0] + [1, 2] + [None, None, None, None] +
                          [3, None, None, None, None, None, None, None])
        self.assertRaises(ValueError, BinaryTree, [0] + [1, 2] +
                          [None, None, None, 3] +
                          [4, None, None, None, None, None, None, None])
        self.assertRaises(ValueError, BinaryTree,
                          [0] + [1, 2] + [None, None, None, 3] + [4])
        self.assertRaises(ValueError, BinaryTree,
                          [0] + [1, 2] + [None, 3, None, None] + [4])

    def test_diameter(self):
        self.assertEqual(6, BinaryTree(self.n1).diameter())
        self.assertEqual(0, BinaryTree(TreeNode(0)).diameter())
        self.assertEqual(1,
                         BinaryTree(TreeNode(0, None, TreeNode(1))).diameter())

    def test_height(self):
        self.assertEqual(5, BinaryTree(self.n1).height())
        self.assertEqual(1, BinaryTree(TreeNode(0)).height())
        self.assertEqual(2, BinaryTree(TreeNode(0, None, TreeNode(1))).height())
        self.assertEqual(3, BinaryTree([3, 9, 20, None, None, 15, 7]).height())

    def test_is_height_balanced(self):
        self.assertEqual(True, BinaryTree([0]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0, 1, None]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0, None, 2]).is_height_balanced())
        self.assertEqual(True, BinaryTree([0, 1, 2]).is_height_balanced())
        self.assertEqual(True, BinaryTree(
            [0] + [1, 2] + [3, None, 4, 5]).is_height_balanced())
        self.assertEqual(True, BinaryTree(
            [3, 9, 20, None, None, 15, 7]).is_height_balanced())
        self.assertEqual(False, BinaryTree(
            [1, 2, 2, 3, 3, None, None, 4, 4, None, None, None, None])
                         .is_height_balanced())

    def test_to_levels(self):
        self.assertEqual(self.n1_levels, BinaryTree(self.n1).to_levels())
        self.assertEqual([[0], [1, 2], [3, None, 4, 5]],
                         BinaryTree([0] + [1, 2] + [3, None, 4, 5]).to_levels())

    def test_width(self):
        self.assertEqual(4, BinaryTree(self.n1).width())
        self.assertEqual(2, BinaryTree([3, 9, 20, None, None, 15, 7]).width())
        self.assertEqual(2, BinaryTree([0, 1, 2]).width())
        self.assertEqual(1, BinaryTree([0]).width())
        self.assertEqual(1, BinaryTree([0, 1, None, 2, None, None, None] +
                                       [None, 2, None, None, None, None, None,
                                        None]).width())

    def test_mirror(self):
        t1_arr = [4, 2, 7, 1, 3, 6, 9]
        t1_bt = BinaryTree(t1_arr)
        t1_bt.mirror()
        t1_mirrored_arr = [4, 7, 2, 9, 6, 3, 1]
        self.assertEqual(t1_mirrored_arr,
                         t1_bt.to_array_view(), "Incorrect mirroring.")
        a1_arr = [4]
        a1_bt = BinaryTree(a1_arr)
        a1_bt.mirror()
        a1_mirrored_arr = [4]
        self.assertEqual(a1_mirrored_arr,
                         a1_bt.to_array_view(), "Incorrect mirroring.")
        b1_arr = [4, 1, None, None, 3]
        b1_bt = BinaryTree(b1_arr)
        b1_bt.mirror()
        b1_mirrored_arr = [4, None, 1, None, None, 3]
        self.assertEqual(b1_mirrored_arr,
                         b1_bt.to_array_view(), "Incorrect mirroring.")

    def test_traverse_inorder(self):
        self.assertEqual([4, 2, 6, 5, 8, 7, 1, 3, 9],
                         BinaryTree(self.n1).traverse_inorder())
        self.assertEqual([2, 4, 1, 5, 3, 6],
                         BinaryTree([1, 2, 3] + [None, 4, 5, 6])
                         .traverse_inorder())
        self.assertEqual([2, 1],
                         BinaryTree([1, 2]).traverse_inorder())
        self.assertEqual([1, 2],
                         BinaryTree([1, None, 2]).traverse_inorder())
        self.assertEqual([1],
                         BinaryTree([1]).traverse_inorder())

    def test_traverse_preorder(self):
        self.assertEqual([1, 2, 4, 5, 6, 7, 8, 3, 9],
                         BinaryTree(self.n1).traverse_preorder())
        self.assertEqual([1, 2],
                         BinaryTree([1, 2]).traverse_preorder())
        self.assertEqual([1, 2],
                         BinaryTree([1, None, 2]).traverse_preorder())
        self.assertEqual([1],
                         BinaryTree([1]).traverse_preorder())

    def test_traverse_postorder(self):
        self.assertEqual([4, 6, 8, 7, 5, 2, 9, 3, 1],
                         BinaryTree(self.n1).traverse_postorder())
        self.assertEqual([2, 1],
                         BinaryTree([1, 2]).traverse_postorder())
        self.assertEqual([2, 1],
                         BinaryTree([1, None, 2]).traverse_postorder())
        self.assertEqual([1],
                         BinaryTree([1]).traverse_postorder())

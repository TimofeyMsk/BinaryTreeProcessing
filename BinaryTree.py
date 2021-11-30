from typing import List, overload


class TreeNode:
    def __init__(self, val, left=None, right=None):
        # if val is None:
        #     raise ValueError('Can not create TreeNode with val = None')
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    """Represent a binary tree as linked set of TreeNode instances.
    Create and return binary tree from existing tree presented by root node
    or by standard array representing.

    b = BinaryTree(TreeNode(0, None, TreeNode(1)) \n
    c = BinaryTree([1] + [2, 3] + [4, 5, None, 9])
    """

    @overload
    def __init__(self, array_view: List[object]):
        """Create and return binary tree from standard array representing.

        :param array_view: standard array representing of tree
        """
        ...

    @overload
    def __init__(self, root: TreeNode):
        """Create and return binary tree from existing tree presented by root node.-

        :param root: root of tree
        """
        ...

    def __init__(self, value: [List[object] | TreeNode]):
        if value is None:
            raise ValueError("Can not create binary tree from None.")
        elif isinstance(value, TreeNode):
            self.__root = value
        elif isinstance(value, List):
            self.__root: TreeNode = BinaryTree.__to_tree_node_view__(value)

    def get_root(self) -> TreeNode:
        """Return root node."""
        return self.__root

    @staticmethod
    def __to_array_view__(root: TreeNode) -> List[object]:
        u"""Convert binary tree to array view.

        Inputed tree will be supplement to full tree with None-nodes. Nodes values
        will be enumerated in array line by line.\n
        ...........1.............[1]\n
        ........./...\\\\............+\n
        ........2....3........[2, 3]\n
        ......./..\\\\................+\n
        .....4....5............[4, 5, None, None]\n
        .............\\\\..............+\n
        ..............6..........[None, None, None, 6, None, None, None, None]\n
        This tree will be convert to [1, 2, 3, 4, 5, None, None, None, None, None, 6, None, None, None, None]

        :param root: root of tree to convert.
        :type root: TreeNode
        :return: array view of tree, defaults to [].
        :rtype: List[object]
        :raises: ValueError if node.val is None.
        :raises: TypeError if root or other node is not instance TreeNode class.
        """


    @staticmethod
    def is_valid_node(node_: TreeNode):
        if not isinstance(node_, TreeNode):
            raise TypeError('Nodes in tree must be TreeNode instances.')
        if node_.val is None:
            raise ValueError('Node.val must not be None')

    def to_levels(self):
        """Return tree node values by levels"""
        if self.__root is None:
            return []
        BinaryTree.is_valid_node(self.__root)
        value_levels: List[object] = []
        current_line_nodes: List[TreeNode] = [self.__root]
        while any(current_line_nodes):
            next_line_nodes: List[TreeNode] = []
            value_level: List[object] = []
            for node in current_line_nodes:

                if node is None:
                    value_level.append(None)
                    next_line_nodes += [None, None]
                    continue
                BinaryTree.is_valid_node(node)
                value_level.append(node.val)
                next_line_nodes += [node.left, node.right]
            value_levels.append(value_level)
            current_line_nodes = next_line_nodes
        return value_levels

    @staticmethod
    def __to_tree_node_view__(array_view: List[object]) -> [TreeNode | None]:
        """Return root of tree presented as linked set of TreeNode instances.

        :param array_view: tree in array view
        :return root: root of tree as TreeNode instance
        :rtype: TreeNode"""

        if array_view is None:
            return None
        if not isinstance(array_view, List):
            raise TypeError('Argument array_view must be List[object].')
        if len(array_view) == 0:
            return None
        # Check count of items
        length = len(array_view)
        line_count = 0
        cur_sum = 0
        while length != cur_sum:
            line_count += 1
            cur_sum += 2 ** (line_count - 1)
            if cur_sum > length:
                raise ValueError('Correct argument array_view must have '
                                 'length equal sum of 2**i where i from 0 to some whole number')

        # Split by tree lines
        lines: List[List[object]] = [array_view[2 ** s - 1: 2 * (2 ** s - 1) + 1]
                                     for s in range(1, line_count)]
        root: TreeNode = TreeNode(array_view[0])
        prev_tn_line: List[TreeNode] = [root]
        for line in lines:
            current_item_i = 0
            new_tn_line: List[TreeNode] = []
            for ptn in prev_tn_line:
                if ptn is None:
                    new_tn_line += [None, None]
                    current_item_i += 2
                    continue
                left_item = line[current_item_i]
                right_item = line[current_item_i + 1]
                ptn.left = None if left_item is None else TreeNode(left_item)
                ptn.right = None if right_item is None else TreeNode(right_item)
                current_item_i += 2
                new_tn_line += [ptn.left, ptn.right]
            prev_tn_line = new_tn_line
        return root

    def diameter(self) -> int:
        """Return diameter of binary tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a
        tree. This path may or may not pass through the root. The length of a path between two
        nodes is represented by the number of edges between them."""
        max_way_length = 0

        # Return (longest_way, longest_branch).
        # longest_way = length of the longest path throw this node.
        # longest_branch = length of the longest patch from this node to some further sheet.
        def node_processing(node: TreeNode) -> (int, int):
            nonlocal max_way_length
            l_w_l, l_b_l, l_w_r, l_b_r = 0, 0, 0, 0
            if not node.left and not node.right:
                # print(node.val, "->", 0, 0)
                return 0, 0
            if node.left:
                l_w_l, l_b_l = node_processing(node.left)
            if node.right:
                l_w_r, l_b_r = node_processing(node.right)
            longest_way = ((l_b_l + 1) if node.left else 0) + ((l_b_r + 1) if node.right else 0)
            # print("longest_way", longest_way)
            # print("Solution.max_way_length", max_way_length)
            max_way_length = max(max_way_length, longest_way)
            longest_branch = max(l_b_l, l_b_r) + 1
            # print(node.val, "->", longest_way, longest_branch)
            return longest_way, longest_branch

        node_processing(self.__root)
        return max_way_length

    def __repr__(self):
        return str(self)

    def height(self) -> int:
        """Return height of binary tree, number of levels below the root.

        A binary tree's height is the number of nodes along the longest
        path from the root node down to the farthest leaf node. """
        maximum = 0

        def go(next_node: TreeNode, cur_depth: int):
            if not next_node.left and not next_node.right:
                cur_depth += 1
                nonlocal maximum
                maximum = max(maximum, cur_depth)
            if next_node.left:
                go(next_node.left, cur_depth + 1)
            if next_node.right:
                go(next_node.right, cur_depth + 1)

        go(self.__root, 0)
        return maximum

    def is_height_balanced(self):
        is_balanced = True

        def go(node: TreeNode) -> int:
            """Return height of tree."""
            nonlocal is_balanced
            if not is_balanced:
                return 0
            height_left_subtree = 0
            height_right_subtree = 0
            if not node.left and not node.right:
                return 1
            if node.left:
                height_left_subtree = go(node.left)
            if node.right:
                height_right_subtree = go(node.right)
            if abs(height_left_subtree - height_right_subtree) > 1:
                is_balanced = False
            return max(height_left_subtree, height_right_subtree) + 1

        go(self.__root)
        return is_balanced

    def width(self):
        pass

    def __str__(self):
        return str(self.__to_array_view__(self.__root))

from typing import List, overload
from math import log2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    """Represent a binary tree as linked set of TreeNode instances"""

    @overload
    def __init__(self, root: TreeNode):
        self.root: TreeNode = root


    @overload
    def __init__(self, array_view: List[object]):
        self.root: TreeNode = BinaryTree.__to_tree_node_view__(array_view)

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

        def check_node(node_: TreeNode):
            if not isinstance(node_, TreeNode):
                raise TypeError('Nodes in tree must be TreeNode instances.')
            if node_.val is None:
                raise ValueError('Node.val must not be None')

        if root is None:
            return []
        check_node(root)
        result: List[object] = []
        current_line_nodes: List[TreeNode] = [root]
        while any(current_line_nodes):
            next_line_nodes: List[TreeNode] = []
            for node in current_line_nodes:
                if node is None:
                    result.append(None)
                    next_line_nodes += [None, None]
                    continue
                check_node(node)
                result.append(node.val)
                next_line_nodes += [node.left, node.right]
            current_line_nodes = next_line_nodes
        return result

    @staticmethod
    def __to_tree_node_view__(array_view: List[object]) -> TreeNode:
        """Return root of tree presented as linked set of TreeNode instances.

        :param array_view: tree in array view
        :return root: root of tree as TreeNode instance
        :rtype: TreeNode"""

        if array_view is None:
            return None
        if not isinstance(array_view, List):
            raise TypeError('Argument array_view must be List[object].')
        lines_count = log2(len(array_view))
        if lines_count != int(lines_count):
            raise ValueError('Correct argument array_view must have length equal to a power of 2.')
        int

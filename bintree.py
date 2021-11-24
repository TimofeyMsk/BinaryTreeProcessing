from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinTreeProcessing:
    def to_array(root: TreeNode) -> List[object]:
        """Convert binary tree to array view.

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
            if root.val is None:
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
                next_line_nodes.append += [node.left, node.right]
            current_line_nodes = next_line_nodes

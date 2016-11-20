"""
Example of a simple binary search tree. Intended for learning purposes
only.
"""


def binary_tree_search(key, node):
    """
    Recursive version of searching a binary tree
    """
    if node is None or node.key == key:
        return node
    elif key < node.key:
        return binary_tree_search(key, node.left)
    else:
        return binary_tree_search(key, node.right)


def binary_tree_search_it(key, node):
    """
    Iterative binary tree search
    """
    MatchingNode = node

    while node is not None:
        if key == MatchingNode.key
            return MatchingNode
        elif key < MatchingNode.key:
            MatchingNode = MatchingNode.left
        else:
            MatchingNode = MatchingNode.right

    return None


def binary_tree_insert(node, key, value):
    """
    Insert a new node into the correct position
    in a binary search tree. Recursively search the tree
    until we find the right position to insert. This version modifies
    the tree in-place.
    """
    if node is None:
        node = Node(key, value)
    elif key < node.key:
        binary_tree_insert(node.left, key, value)
    else:
        binary_tree_insert(node.right, key, value)


 def binary_tree_insert_persistent(node, key, value):
     """
     Another insert function for a binary tree. This one retains
     the original tree.
     """
    if node is None:
        return NodeTree(None, key, value, None)

    if key == node.key:
        return NodeTree(node.left, key, value, node.right)

    if key < node.key:
        return NodeTree(binary_tree_insert(node.left, key, value), node.key, node.value, node.right)
    else:
        return NodeTree(node.left, node.key, node.value, binary_tree_insert(node.right, key, value))


def binary_tree_min(node):
    """
    Find the minimum value in a binary tree.
    """
    if node.left is None:
        return node
    else:
        return binary_tree_min(node)


def binary_tree_min_it(node):
    """
    As above, but iterative rather than recursive
    """
    current_node = node

    while current_node.left is not None:
        current_node = current_node.left

    return current_node





def replace_node_in_parent(self, new_value=None):
    if self.parent:
        if self == self.parent.left_child:
            self.parent.left_child = new_value
        else:
            self.parent.right_child = new_value
    if new_value:
        new_value.parent = self.parent

def binary_tree_delete(self, key):
    if key < self.key:
        self.left_child.binary_tree_delete(key)
    elif key > self.key:
        self.right_child.binary_tree_delete(key)
    else: # delete the key here
        if self.left_child and self.right_child: # if both children are present
            successor = self.right_child.find_min()
            self.key = successor.key
            successor.binary_tree_delete(successor.key)
        elif self.left_child:   # if the node has only a *left* child
            self.replace_node_in_parent(self.left_child)
        elif self.right_child:  # if the node has only a *right* child
            self.replace_node_in_parent(self.right_child)
        else: # this node has no children
            self.replace_node_in_parent(None)

"""
Simple implementation of depth-first search.
"""
import unittest


class Node(object):

    def __init__(self, value, neighbours=[]):
        self.value = value
        self.neighbours = neighbours

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return self.__repr__()


def neighbours_of(node):
    """
    Return a list of all neighbours of a given
    node, i.e. all nodes which are connected to it by
    edges
    """
    return node.neighbours


def depth_first_search(start_node):
    """
    """
    visited = set([start_node])
    print start_node
    visit_nodes(start_node, visited)


def visit_nodes(start_node, visited):
    for node in neighbours_of(start_node):
        if node not in visited:
            print node
            visited.add(node)
            visit_nodes(node, visited)


class TestDepthFirstSearch(unittest.TestCase):

    def test_reaches_all_nodes_in_connected_graph(self):
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)
        node_6 = Node(6)
        node_7 = Node(7)

        node_1.neighbours = [node_2, node_3]
        node_2.neighbours = [node_3, node_1, node_4]
        node_3.neighbours = [node_5]
        node_4.neighbours = [node_6]
        node_5.neighbours = [node_7]

        depth_first_search(node_1)



if __name__ == "__main__":
    unittest.main()

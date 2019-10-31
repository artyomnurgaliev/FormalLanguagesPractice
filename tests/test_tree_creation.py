import solution


def test_tree_creation():
    node = solution.Node()
    tree = solution.Tree(node)
    assert tree.root == node
    assert tree.curr_nodes.pop() == node

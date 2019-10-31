import solution


def test_node_creation():
    node = solution.Node()
    assert node.symbol == '1'
    assert node.parents.__class__ == set().__class__
    assert node.transitions.__class__ == set().__class__


def test_adding_parent():
    node = solution.Node()
    parent = solution.Node()
    node.add_parent(parent)
    assert node.parents.pop() == parent


def test_adding_transition():
    node = solution.Node()
    new_node = solution.Node()
    node.add_transition(new_node)
    assert node.transitions.pop() == new_node

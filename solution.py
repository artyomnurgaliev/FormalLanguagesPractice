import sys

OPERATION_SYMBOLS = ('.', '+', '*')
ALPHABET_SYMBOLS = ('a', 'b', 'c', '1')


class Node:
    def __init__(self, symbol='1'):
        self.transitions = set()
        self.symbol = symbol
        self.parents = set()

    def add_parent(self, parent):
        self.parents.add(parent)

    def add_transition(self, node):
        self.transitions.add(node)


class Tree:
    def __init__(self, node):
        self.root = node
        self.curr_nodes = set()
        self.curr_nodes.add(self.root)


def dfs(node, string, max_len_of_suffix):
    k = max_len_of_suffix + 1
    if len(string) == 0:
        return max_len_of_suffix
    symbol = string[-1]
    if node.symbol != '1':
        string = string[:-1]
    else:
        k -= 1
    if node.symbol == symbol or node.symbol == '1':
        if len(node.parents) == 0:
            return k
        for parent in node.parents:
            max_len_of_suffix = max(dfs(parent, string, k), max_len_of_suffix)
    return max_len_of_suffix


class RegularExpression:
    def __init__(self, string):
        self.error = False
        self.stack = []
        for symbol in string:
            if symbol in ALPHABET_SYMBOLS:
                self.stack.append(Tree(Node(symbol)))
            elif symbol in OPERATION_SYMBOLS:
                if symbol == '.':
                    if len(self.stack) < 2:
                        self.error = True
                        break
                    else:
                        self.concatenation()
                if symbol == '*':
                    if len(self.stack) < 1:
                        self.error = True
                        break
                    else:
                        self.klini_closure()
                if symbol == '+':
                    if len(self.stack) < 2:
                        self.error = True
                        break
                    else:
                        self.add()
            else:
                self.error = True
                break

    def add(self):
        x = self.stack.pop()
        y = self.stack.pop()
        new_node = Node()
        new_tree = Tree(new_node)
        new_tree.curr_nodes = set()

        new_tree.root.add_transition(x.root)
        new_tree.root.add_transition(y.root)
        x.root.add_parent(new_tree.root)
        y.root.add_parent(new_tree.root)

        for node in x.curr_nodes:
            new_tree.curr_nodes.add(node)

        for node in y.curr_nodes:
            new_tree.curr_nodes.add(node)

        self.stack.append(new_tree)

    def concatenation(self):
        y = self.stack.pop()
        x = self.stack.pop()
        for node in x.curr_nodes:
            node.add_transition(y.root)
            y.root.add_parent(node)
        x.curr_nodes = y.curr_nodes
        self.stack.append(x)

    def klini_closure(self):
        x = self.stack.pop()
        new_node = Node()
        new_tree = Tree(new_node)
        new_tree.curr_nodes = set()
        new_tree.root.add_transition(x.root)
        x.root.add_parent(new_tree.root)
        for node in x.curr_nodes:
            node.add_transition(new_tree.root)
            new_tree.root.add_parent(node)
        new_tree.curr_nodes.add(new_tree.root)

        self.stack.append(new_tree)

    def calculate_result(self, string):
        tree = self.stack.pop()
        k = 0
        max_len_of_suffix = 0
        for node in tree.curr_nodes:
            max_len_of_suffix = max(dfs(node, string, k), max_len_of_suffix)
        print(max_len_of_suffix)


def process_input():
    input_string = input().split()
    alpha = input_string[0]
    u = input_string[1]
    return alpha, u


def calc_result(alpha, u):
    regular_expression = RegularExpression(alpha)
    if len(regular_expression.stack) != 1:
        regular_expression.error = True
    if regular_expression.error:
        print("ERROR")
    else:
        regular_expression.calculate_result(u)


if __name__ == '__main__':
    input_res = process_input()
    calc_result(input_res[0], input_res[1])

class Tree:
    def __init__(self, label, branches=[]):
        assert all([isinstance(b, Tree) for b in branches])
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches


def fib_tree(n):
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n - 1)
        right = fib_tree(n - 2)
        return Tree(left.label + right.label, [left, right])


def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        all_leaves = []
        for b in t.branches:
            all_leaves.extend(leaves(b))
        return all_leaves


def height(t):
    if t.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in t.branches])


fib_6 = fib_tree(6)
print('Leaves:', leaves(fib_6))
print(sum(leaves(fib_6)) == fib_6.label)
print('Height:', height(fib_6))

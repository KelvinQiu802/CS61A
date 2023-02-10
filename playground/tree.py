# Trees

def tree(root_label, branches=[]):
    """Construct the tree ADT.

    >>> tree(0, [tree(1), tree(2)])
    [0, [1], [2]]
    >>> tree(1, [tree(2), tree(3, [tree(4)])])
    [1, [2], [3, [4]]]
    >>> tree(10)
    [10]
    """
    for branch in branches:
        assert is_tree(branch), 'branch must be tree'
    return [root_label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    return not branches(tree)

# Process Tree


def count_leaves(tree):
    """Count the number of leaves in the tree.

    >>> tree = tree(1, [tree(2), tree(3, [tree(4)])])
    >>> count_leaves(tree)
    2
    """
    if is_leaf(tree):
        return 1
    branch_counts = [count_leaves(b) for b in branches(tree)]
    return sum(branch_counts)

def reduce(fn, lst, init):
    """Reduce Higher Order Function

    >>> reduce(lambda x, y: x * y, [1, 2, 3, 4], 1)
    24
    """
    if not lst:
        return init
    return reduce(fn, lst[1:], fn(init, lst[0]))

# 当需要记录递归过程中的一些状态时，可以尝试引入helper函数

def max_lst(lst):
    """Return the maximum number in the lst.

    >>> max_lst([1, 2, 3, -1, 9])
    9
    """
    def helper(lst, max):
        if not lst:
            return max
        if lst[0] > max:
            return helper(lst[1:], lst[0])
        return helper(lst[1:], max)
    return helper(lst, lst[0])

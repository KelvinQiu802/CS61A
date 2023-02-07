def adder(x):
    def f(y):
        return x + y
    return f


add_three = adder(3)
print(add_three(4))
print('=================')


def print_sum(x):
    print(x)

    def next_sum(y):
        return print_sum(x + y)
    return next_sum


print_sum(4)(4)(1)
print('=================')


def logger(f):
    def logged_f(*args):
        print('The return value of [', f.__name__, '] is', f(*args))
    return logged_f


logged_abs = logger(abs)
logged_abs(1)
logged_abs(2)

print('=================')

# Self Referencing Function


def do_all(f):
    def do_next(g):
        if g == 'done':
            return f
        return do_all(compose(f, g))
    return do_next


def compose(f, g):
    def composed(x):
        return g(f(x))
    return composed


add_one_mul_two = do_all(lambda x: x + 1)(lambda x: x * 2)('done')
print(add_one_mul_two(2))

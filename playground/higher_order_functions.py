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

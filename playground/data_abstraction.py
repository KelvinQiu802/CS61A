from math import gcd


def add_rational(r1, r2):
    """Calculate the addition of two rationals.

    >>> r1 = rational(1, 2)
    >>> r2 = rational(2, 3)
    >>> add_rational(r1, r2)
    [7, 6]
    """
    return rational(numer(r1) * denom(r2) + numer(r2) * denom(r1), denom(r1) * denom(r2))


def mul_rational(r1, r2):
    """Calculate the multiplication of two rationals.

    >>> r1 = rational(1, 2)
    >>> r2 = rational(2, 3)
    >>> mul_rational(r1, r2)
    [1, 3]
    """
    return rational(numer(r1) * numer(r2), denom(r1) * denom(r2))


def rational(n, d):
    """Construct a rational number x that represents n/d.

    >>> rational(2, 3)
    [2, 3]
    >>> rational(5, 10)
    [1, 2]
    """
    g = gcd(n, d)
    return [n // g, d // g]


def numer(r):
    """Return the numerators of the input rational

    >>> numer(rational(2, 3))
    2
    """
    return r[0]


def denom(r):
    """Return the denominator of the input rational

    >>> denom(rational(2, 3))
    3
    """
    return r[1]

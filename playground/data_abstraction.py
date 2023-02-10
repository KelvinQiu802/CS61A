from math import gcd


def add_rational(r1, r2):
    """Calculate the addition of two rationals.

    >>> r1 = rational(1, 2)
    >>> r2 = rational(2, 3)
    >>> result = add_rational(r1, r2)
    >>> print_rational(result)
    7 / 6
    """
    n_r1, d_r1 = numer(r1), denom(r1)
    n_r2, d_r2 = denom(r1), denom(r2)
    return rational(n_r1 * d_r2 + n_r2 * d_r1, d_r1 * d_r2)


def mul_rational(r1, r2):
    """Calculate the multiplication of two rationals.

    >>> r1 = rational(1, 2)
    >>> r2 = rational(2, 3)
    >>> result = mul_rational(r1, r2)
    >>> print_rational(result)
    1 / 3
    """
    return rational(numer(r1) * numer(r2), denom(r1) * denom(r2))


def calc_rational(r):
    """Calculate the rational to float.

    >>> calc_rational(rational(1, 2))
    0.5
    >>> calc_rational(rational(2, 1))
    2.0
    """
    return numer(r) / denom(r)


def print_rational(r):
    """Print the rational.

    >>> print_rational(rational(1, 2))
    1 / 2
    """
    print(numer(r), '/', denom(r))


def rational(n, d):
    """Construct a rational number x that represents n/d.

    >>> print_rational(rational(2, 3))
    2 / 3
    >>> print_rational(rational(5, 10))
    1 / 2
    """
    g = gcd(n, d)

    def selector(name):
        if name == 'n':
            return n // g
        elif name == 'd':
            return d // g
    return selector


def numer(r):
    """Return the numerators of the input rational

    >>> numer(rational(2, 3))
    2
    """
    return r('n')


def denom(r):
    """Return the denominator of the input rational

    >>> denom(rational(2, 3))
    3
    """
    return r('d')

from math import sqrt

def has_sqrt(x):
  return x > 0 and sqrt(x)

def reasonable(n):
  return n == 0 or 1/n != 0
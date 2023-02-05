from operator import floordiv, mod

def devide_exact(n, d = 1):
  """This is the Doc
  
  >>> q, r = devide_exact(2013, 10)
  >>> q
  201
  >>> r
  3
  """
  return floordiv(n, d), mod(n, d)

q, r = devide_exact(2023, 10)

print(q, r)
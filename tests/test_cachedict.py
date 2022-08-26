
from betterdicts import cache_dict

def foo(n):
  "Docstring"
  return 2*n

def test_cache_dict1():
  cf = cache_dict(foo)

  assert cf(10) == 20
  assert len(cf) == 1
  assert cf[10] == 20

  assert cf[20] == 40
  assert cf.__doc__ == 'Docstring'

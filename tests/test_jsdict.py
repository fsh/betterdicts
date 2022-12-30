
import pytest
from betterdicts import jsdict, attr_dict

def test_basic():
  dic = jsdict(a=1, b=2, c=3)

  assert dic.a == 1
  assert dic['b'] == 2
  assert hasattr(dic, 'c')
  dic.d = 50
  assert dic['d'] == 50
  dic['e'] = 60
  assert dic.e == 60
  assert dic == {'a':1, 'b':2, 'c':3, 'd':50, 'e':60}

def test_attrdict():
  dic = attr_dict(a=1, b=2, c=3)

  assert dic.a == 1
  assert dic['b'] == 2
  assert hasattr(dic, 'c')
  dic.d = 50
  assert dic['d'] == 50
  dic['e'] = 60
  assert dic.e == 60
  assert dic == {'a':1, 'b':2, 'c':3, 'd':50, 'e':60}

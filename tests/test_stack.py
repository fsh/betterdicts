
from betterdicts import stack_dict

def test_stack():

  dic = stack_dict(a=1, b=2, c=3)


  dic.push_stack()

  dic['a'] = 2
  dic['d'] = 4
  assert dic['a'] == 2

  dic.pop_stack()

  assert dic['a'] == 1
  assert 'd' not in dic

import pytest
from betterdicts import betterdict

def even_odd(x):
  return ['even', 'odd'][x&1]

@pytest.fixture(name='d')
def basic_betterdict():
  d = betterdict()

  assert isinstance(d, dict)
  assert d == {}
  assert not d

  assert d.cache_get(2, even_odd) == 'even'
  assert d.cache_get(3, even_odd) == 'odd'

  assert d == {2: 'even', 3: 'odd'}

  assert d.cache_get(2, lambda _: 'NOT RUN') == 'even'

  assert d.insert(0, 'even') is None
  assert d[0] == 'even'

  assert d.insert(0, 'zero') == 'even'
  assert d[0] == 'zero'

  assert d.insert(668, "ba'al", "beelzebub") == "beelzebub"
  assert d[668] == "ba'al"
  del d[668]

  assert len(d) == 3

  return d.copy()

def test_creation(d):
  assert betterdict(d) is not d
  assert betterdict(d) == d
  assert betterdict(d.items()) == d

def test_invert(d):
  assert d.invert() == {'zero': 0, 'even': 2, 'odd': 3}
  assert d.invert().invert() == d

def test_update(d):
  assert d.update(foo='A', bar='B') is d
  assert d['bar'] == 'B'
  assert len(d) == 5

  tmp = d.copy()
  assert tmp.clear().update(d.items()) == d

def test_multidict(d):
  duplist = list(d.disperse())

  md = betterdict.collect(list, duplist)
  assert md == {0: ['z', 'e', 'r', 'o'], 2: ['e', 'v', 'e', 'n'], 3: ['o', 'd', 'd']}
  assert betterdict.collect(list, duplist) == md
  assert betterdict.collect(set, duplist) == {0: {'z', 'e', 'r', 'o'}, 2: {'e', 'v', 'n'}, 3: {'o', 'd'}}

  assert betterdict.collect(list, duplist, lambda c, v: c.insert(0, v)) \
    == md.map_values(lambda v: v[::-1])

  tmp = md.copy().map_values(list.copy)
  assert tmp.collect(duplist) == md.map_values(lambda v: v * 2)
  assert tmp == md.map_values(lambda v: v * 2)

  assert betterdict.combine(min, duplist) == {0: 'e', 2: 'e', 3: 'd'}
  assert betterdict.combine(str.__add__, duplist) == d

  tmp = md.copy()
  assert md.combine(list.__add__, md.items()) == md.map_values(lambda v: v * 2)

  test = [(even_odd(x), x) for x in range(5)]

  combined = betterdict.combine(int.__add__, test)
  assert combined == {'even': 6, 'odd': 4}

  collected = betterdict.collect(list, test)
  assert collected == {'even': [0,2,4], 'odd': [1,3]}

  assert betterdict.collect(list, collected.disperse()) == collected

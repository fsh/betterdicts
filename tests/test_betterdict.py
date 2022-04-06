
from betterdicts import betterdict

def test_init_collate():
  b1 = betterdict(((i%2, i) for i in range(10)), collate=True)
  assert b1[0] == {0,2,4,6,8}
  b2 = betterdict(((i%2, i) for i in range(10)), collate=list)
  assert b2[1] == [1,3,5,7,9]
  assert 2 not in b1 and 2 not in b2

def test_collate():
  b1 = betterdict()
  b1.collate( ((i%2, i) for i in range(10)) )
  assert b1[0] == {0,2,4,6,8}

  b1.collate( [(0,'a'),(1,'b'),(2,'c')] )
  assert b1[2] == {'c'}
  assert b1[0] == {0,2,4,6,8,'a'}

def test_invert():
  b = betterdict((i, i%2) for i in range(10))

  b1 = b.invert()
  assert len(b1) == 2
  assert set(b1.keys()) == {0,1}
  assert b1[1] in {1,3,5,7,9}

  b2 = b.invert(collate=list)
  assert b2[0] == [0,2,4,6,8]
  assert 2 not in b2

  b3 = b.invert(collate=set)
  assert b3[0] == {0,2,4,6,8}

import tempfile

from betterdicts import persistent_dict

def test_persisent():
  fname = tempfile.mktemp()
  dic = persistent_dict(fname)

  assert len(dic) == 0
  dic[1] = 2

  assert persistent_dict(fname) == {1: 2}

  del dic

  fname2 = tempfile.mktemp()
  dic = persistent_dict(fname2)

  assert len(dic) == 0
  dic = persistent_dict(fname)

  assert dic == {1: 2}

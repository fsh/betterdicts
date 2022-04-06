"""The `betterdict` utility class.

It inherits from `dict` but adds various convenience method for inversion,
filtering, mapping, and collating.

"""


class betterdict(dict):
  """`betterdict` is a `dict` with a few extra utility methods.

  Extra methods include:

  `invert()`, `collate(it, type=t)`, `filter(keys=None, values=None)`, `map(keys=None, values=None, collate=None)`

  """

  def __init__(self, arg=None, /, collate=None):
    if collate is not None:
      if arg is None:
        raise ValueError("must be given an argument if collate is used")
      if collate is True:
        collate = set
      super().__init__()
      self.collate(arg, type=collate)
    elif arg is not None:
      super().__init__(arg)
    else:
      super().__init__()

  def copy(self):
    return self.__class__(super().copy())

  def invert(self, /, collate=None):
    """Invert keys and values, returning a dictionary that maps values to keys.

    If the optional parameter `collate` is a collection type, then keys that map
    to the same value will be collected into that type. `collate` can also be
    given `True` in which case it will default into using the `set` type.

    >>> betterdict((i, i**2) for i in range(10)).invert()
    {0: 0, 1: 1, 4: 2, 9: 3, 16: 4, 25: 5, 36: 6, 49: 7, 64: 8, 81: 9}

    """
    if collate is True:
      collate = set
    if collate is not None:
      return self.__class__(((v,k) for k,v in self.items()), collate=collate)
    return self.__class__({v:k for k,v in self.items()})

  def collate(self, it, type=set):
    """Works like a `dict.extend()` for dictionaries where the values are collections.

    Instead of duplicate keys being overwritten, they are added or appended to
    their respective collection.

    The optional keyword parameter `type` specifies the collection type. It
    defaults to `set`. It currently accepts subclasses of `list` or `set`, which
    determines whether it adds elements with `.append()` or `.add()`.

    Returns `self`.

    >>> betterdict().collate((i%5, i**2) for i in range(20))
    {0: [0, 25, 100, 225], 1: [1, 36, 121, 256], 2: [4, 49, 144, 289], 3: [9, 64, 169, 324], 4: [16, 81, 196, 361]}

    """
    if isinstance(it, dict):
      it = it.items()
    if issubclass(type, list):
      f = type.append
    elif issubclass(type, set):
      f = type.add
    else:
      raise ValueError(f"unknown type {type.__name__}")
    for k,v in it:
      if k in self:
        f(self[k], v)
      else:
        self[k] = type((v,))
    return self

  def filter(self, keys=None, values=None):
    """Filter keys or values, returning a new dictionary.

    This method covers many use cases depending on how it's used:

    - filter()

      Filters k=>v pairs where bool(v) is true.

    - filter(keys=f) or filter(f)

      Filters k=>v pairs where f(k) evaluates to true.

    - filter(values=f) or filter(None, f)

      Filters k=>v pairs where f(v) evaluates to true.

    - filter(f,g) or filter(keys=f, values=g)

      Filters k=>v pairs where f(k) *and* g(v) evaluates to true.

    """
    if keys is None and values is None:
      values = bool
    return self.__class__({
      k:v for k,v in self.items()
      if (keys is None or keys(k)) and (values is None or values(v))
    })

  def map(self, keys=None, values=None, collate=None):
    """Map keys or values, returning a new dictionary.

    """
    if keys is None and values is None:
      raise ValueError("specify one of keys or values to map")
    if collate is True:
      collate = set
    if keys is None:
      keys = lambda x: x
    if values is None:
      values = lambda x: x
    return self.__class__(((keys(k), values(v)) for k,v in self.items()), collate=collate)

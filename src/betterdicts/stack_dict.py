from betterdicts import betterdict


class stack_dict(betterdict):
  """A stack dictionary is like a stack of dictionaries.

  Also known as scoped dictionary, or a multi-level dictionary.

  The current state of the dictionary can be saved with `push_stack()` and
  restored later with `pop_stack()`. Any changes made to the dictionary between these
  function calls will be discarded.

  The dictionary can also be flattened.

  Otherwise it behaves like a normal `betterdict`.

  This kind of dictionary is useful for representing scopes or namespaces, where
  inner namespaces can shadow earlier definitions.  It is also similar to how
  lookup on Python works by checking base classes etc.

  *Implementation details*: `stack_dict` works in-place, meaning that
  if you have two references to the same `stack_dict` then moving up/down the
  stack on one will be reflected in the other as well. `stack_dict` also stores
  a flattened version of the stack at every level. This is the most efficient,
  but will potentially waste a lot of memory for deep stacks with many entries.
  The alternative of storing only the "difference" between each stack is an
  order of magnitude slower for similarly structures.

  *Note*: It's also possible to abuse Python's dynamic types to implement this
  functionality via the bulit-in class hiearchy (e.g. subclass from `type` and
  you can do `type('', (cur,), new_entries)`), but it's a bit finicky and
  probably not sane.

  """

  __slots__ = ('_last', )

  @property
  def previous(self):
    """The previous state or `None` if we have no previous state.

    """
    return self._last

  def is_root(self):
    """Returns `True` if there's no previous stack entry.

    """
    return self._last is None

  def __init__(self, *args, _last=None, **kwargs):
    super().__init__(*args, **kwargs)
    self._last = _last

  def copy(self):
    return stack_dict(self, _last=self._last)

  def push_stack(self, *args, **kwargs):
    """Saves the current state and updates the dictionary with the given
    arguments (as if calling `update()`).

    This update, as well as any subsequent changes will be discarded when
    `pop_stack()` is called.

    A push should always be paired with an eventual pop to prevent memory leaks.

    """
    self._last = self.copy()
    self.update(*args, **kwargs)

  def pop_stack(self):
    """Restore the dictionary to its previous state.

    Raises `IndexError` if there's no previous state.

    """
    if self._last is None:
      raise IndexError("stack is empty")
    self.clear()
    if self._last is not None:
      self.update(self._last)
      self._last = self._last._last

  def flatten_stack(self):
    """Flattens the dictionary, removing any references to previous states.

    After this it becomes invalid to call `pop_stack()`.

    """
    self._last = None

  def __enter__(self):
    self.push_stack()
    return self

  def __exit__(self, typ, exc, tb):
    if self._last is not None: # we might have been flattened.
      self.pop_stack()

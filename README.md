# betterdicts

## betterdict

``` python
from betterdicts import betterdict
```

Works just like a dict, but has some extra useful methods:

- invert()
  
  Inverts a mapping, turning values into keys and vice-versa.
  
- collate(it, type=list)

  Collects repeated keys into sets or lists depending on the `type` argument.
  
- filter(keys=None, values=None)

  Filters keys, values, or both.
  
- map(keys=None, values=None)

  Map keys, values, or both.

## jsdict, njsdict, rjsdict

``` python
from betterdicts import jsdict, njsdict, rjsdict
```

These are `betterdict`s but works like JavaScript object, where keys and
attributes are the same. This is accomplished with zero overhead.

These can be very convenient when working with parameters, configuration,
settings, or the like, where the `obj['key']` or `obj.get('key')` access method
feels a bit overly verbose for the simple task at hand.

## number_dict

Acts like a `collections.Counter()` with arithmetic support like a number.

``` python-console
>>> q = number_dict(range(5))
>>> q
{0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
>>> q[1] += 5
>>> q[4] += 1
>>> q[9]
0
>>> q[9] = 9
>>> (q+1)**2
{0: 4, 1: 49, 2: 4, 3: 4, 4: 9, 9: 100}
>>> 1 / q
{0: 1.0, 1: 0.16666666666666666, 2: 1.0, 3: 1.0, 4: 0.5, 9: 0.1111111111111111}
```

## persistent_dict

The simplest possible persistent state exposed as a dict.

This is for when you need something really simple to store some flat data
between script invocations, without the extra management of databases or file
formats or the like.

Any change made directly to the dictionary[^1] causes it to save itself to disk
as a pickle file. Whenever an instance is created of this dictionary it will
load the same file.

The file defaults to `cache.pickle` in the current working directory, but can be
specified as a parameter with `persistent_dict(cache_file=<FILENAME>)`.

[^1]: "deep" changes like to objects stored in the dictionary are not tracked

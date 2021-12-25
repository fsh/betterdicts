# betterdicts

## betterdict

``` python
from betterdicts import betterdict
```

Works just like a dict, but has some extra useful methods:

- invert()
- collate(it, type=list)
- filter(keys=None, values=None)

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

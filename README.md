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

## autopickled_dict



try:
  from .VERSION import __version__
except:
  __version__ = 'failed to load VERSION.py file'

from .betterdict import betterdict
from .jsdict import attr_dict, jsdict, njsdict, rjsdict
from .persistent import persistent_dict
from .number_dict import number_dict
from .dynamic_dict import dynamic_dict, cache_dict
from .stack_dict import stack_dict

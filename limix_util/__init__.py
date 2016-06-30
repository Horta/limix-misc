import pkg_resources
try:
    __version__ = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = 'unknown'

from . import dict
from . import hdf5
from . import inspect
from . import object
from . import path
from . import pickle
from . import report
from . import scalar
from . import set
from . import string
from . import sys
from . import time

import pkg_resources
__version__ = pkg_resources.get_distribution(__name__).version

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

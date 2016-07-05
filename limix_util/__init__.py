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

from . import dict as dict_
from . import hdf5 as hdf5_
from . import inspect as inspect_
from . import object as object_
from . import path as path_
from . import pickle as pickle_
from . import report as report_
from . import scalar as scalar_
from . import set as set_
from . import string as string_
from . import sys as sys_
from . import time as time_

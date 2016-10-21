from __future__ import absolute_import

from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound

try:
    __version__ = get_distribution('limix-util').version
except DistributionNotFound:
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


def test():
    import os
    p = __import__('limix_util').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main(['-q'])
    finally:
        os.chdir(old_path)

    if return_code == 0:
        print("Congratulations. All tests have passed!")

    return return_code

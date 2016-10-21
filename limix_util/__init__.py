from pkg_resources import get_distribution
from pkg_resources import DistributionNotFound

try:
    __version__ = get_distribution('limix-util').version
except DistributionNotFound:
    __version__ = 'unknown'

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

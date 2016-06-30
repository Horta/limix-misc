from __future__ import division, print_function
import os
import sys
from setuptools import setup, find_packages

PKG_NAME = 'limix_util'
VERSION  = '0.0.12'

def module_exists(module_name):
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

def setup_package():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    os.chdir(src_path)
    sys.path.insert(0, src_path)

    install_requires = ['humanfriendly', 'progressbar', 'asciitree']
    setup_requires = []

    metadata = dict(
        name=PKG_NAME,
        maintainer="Limix Developers",
        version=VERSION,
        maintainer_email="horta@ebi.ac.uk",
        packages=find_packages(),
        license="BSD",
        url='http://pmbio.github.io/limix/',
        install_requires=install_requires,
        setup_requires=setup_requires,
        zip_safe=True
    )

    try:
        from distutils.command.bdist_conda import CondaDistribution
        metadata['distclass'] = CondaDistribution
        metadata['conda_buildnum'] = 1
    except ImportError:
        pass

    try:
        setup(**metadata)
    finally:
        del sys.path[0]
        os.chdir(old_path)

if __name__ == '__main__':
    def err_msg(name):
        msg = "Error: %s package couldn't be found." % name
        msg += " Please, install it first so I can proceed."
        return msg

    for pn in ['numpy', 'hdf5']:
        if not module_exists(pn):
            print(err_msg(pn))
            sys.exit(1)

    setup_package()

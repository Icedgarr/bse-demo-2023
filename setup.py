try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import bse_demo_library


def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setup(
    name='bse_demo_library',
    version=bse_demo_library.__version__,
    description='Example library',
    author='Roger',
    packages=find_packages(where='', exclude=['tests']),
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='https://github.com/icedgarr/bse-demo-2024',
    classifiers=[
        'Programming Language :: Python :: 3.10.7'
    ]
)

import os # noqa
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

path, script = os.path.split(sys.argv[0])
os.chdir(os.path.abspath(path))

install_requires = []

install_requires.append('requests')
install_requires.append('jsonpickle')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'cardconnect'))


setup(
    name='cardconnect',
    cmdclass={'build_py': build_py},
    version='1.0.0',
    description='CardConnect Python SDK',
    author='CardConnect',
    packages=['cardconnect', 'cardconnect.test'],
    install_requires=install_requires,
    test_suite='cardconnect.test.all',
    tests_require=['unittest2', 'mock'],
    use_2to3=True)

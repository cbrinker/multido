from distutils.core import setup

setup(
    name='multido',
    version='0.1.0',
    author='Chris Brinker',
    author_email='chris.brinker@gmail.com',
    packages=['multido', 'multido.test'],
    scripts=['bin/multido'],
    url='http://pypi.python.org/pypi/multido/',
    license='LICENSE.txt',
    description='Useful utility to easily run a command in parallel and understand any failures that may have occurred',
    long_description=open('README.txt').read(),
)

from setuptools import setup

from simple_ioc import get_version

setup(
    name='simple-ioc',
    version=get_version(),
    license='GPLv3',
    author='Agroptima S.L.',
    author_email='developers@agroptima.com',
    description='A lightweight library with an implementation of IoC',
    long_description=open('README.md').read(),
    url='https://github.com/agroptima/simple-ioc',
    download_url='https://github.com/agroptima/simple-ioc/releases',
    keywords=['python', 'dependency-injection', 'inversion-of-control'],
    packages=['simple_ioc'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)

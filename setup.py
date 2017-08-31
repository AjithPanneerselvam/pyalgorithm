from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyalgorithm',
    version='1.2.0',

    description='Algorithm library',
    long_description="Why code? when it is already available!",

    # The project's main homepage.
    url='https://github.com/AjithPanneerselvam/pyalgorithm.git',

    # Author details
    author='Ajith Panneerselvam',
    author_email='ajithpanneerselvam@live.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        # Python version supported
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='Primitive library for algorithms',

    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    packages=find_packages(exclude=['tests']),

    # List run-time dependencies here.  These will be installed by pip when
    install_requires=['peppercorn', 'pytest'],

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    # If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'pyalgorithm': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)

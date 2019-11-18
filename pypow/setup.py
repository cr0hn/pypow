from os import path
from os.path import join
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(join(here, 'requirements.txt')) as f:
    required = f.read().splitlines()

setup(
    name='pypow',
    version="1.0.2",
    packages=find_packages(),
    description='PyPow! is the easy way to expose any cli c'
                'ommand as a REST API.',
    long_description="PyPow! is the easy way to expose any "
                     "cli command as a REST API.",
    install_requires=required,
    extras_require={
        'performance': ["uvloop==0.13.0"]
    },
    include_package_data=True,
    zip_safe=True,
    url='https://github.com/cr0hn/pypow',
    license='Apache 2.0',
    author='Maintainer: cr0hn, Authors: Roberto Martinez, Cesar Gallego, '
           'Hector Ruesca, Pancho Horrillo',
    entry_points={'console_scripts': [
        'kapow = pypow.__main__:kapow'
    ]},
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
    ],
)


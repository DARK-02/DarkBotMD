import os
import re
from setuptools import setup, find_packages
INSTALL_REQUIRES = ['requests',
                    'phonenumbers',
                    'instaloader',
                    'pycoingecko'
                    ]
setup(
install_requires=INSTALL_REQUIRES
)

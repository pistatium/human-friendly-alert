# coding: utf-8

import os
import sys
from setuptools import setup, find_packages
from pip.req import parse_requirements

setup(
    name='human_friendly_alert',
    version='0.0.1',
    url='https://github.com/pistatium/human_friendly_alert',
    author='pistatium',
    description='Human friendly lert manager',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        str(i.req) for i in parse_requirements(
            os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=False) if not i.link
    ],
    entry_points={
        'console_scripts': [
            'human_friendly_alert=human_friendly_alert.cmd:main'
        ]
    },
)


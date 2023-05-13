#!/usr/bin/env python3

version = "1.0.9"

## version 1.0.9 - 14.05.2023
## version 1.0.8 - 14.05.2023
## version 1.0.7 - 14.05.2023

"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    # https://packaging.python.org/specifications/core-metadata/#name
    name='revshell-generator',  # Required

    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,  # Required

    # https://packaging.python.org/specifications/core-metadata/#summary
    description='Reverse shell commands generator',  # Optional

    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional

    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type='text/markdown',  # Optional (see note above)

    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url='https://github.com/totekuh/revshell-generator',  # Optional

    author='totekuh',  # Optional

    author_email='totekuh@protonmail.com',  # Optional

    classifiers=[  # Optional
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='pentest, red-team, shell',  # Optional

    package_dir={'': './src'},  # Optional

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.6, <4',

    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'termcolor',
        'netifaces'
    ],  # Optional

    entry_points={  # Optional
        'console_scripts': [
            'revshell-generator=reverseshellgenerator.generator:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/totekuh/revshell-generator/issues',
        'Source': 'https://github.com/totekuh/revshell-generator',
    },
)

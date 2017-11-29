try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from spass.version import version

config = {
    'description': 'spass - Smart password manager',
    'version': version,
    'packages': ['spass'],
    'scripts': [],
    'name': 'spass',
    'entry_points': {
        'console_scripts': [
            'spass = spass.__main__:main'
        ]
    },
}

setup(**config)

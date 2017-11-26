try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'spass - Smart password manager',
    'version': '0.3',
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

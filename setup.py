from setuptools import setup

setup(
        name = 'fnr',
        version = '0.1.1',
        packages = ['fnr'],
        entry_points = {
            'console_scripts': [
                'fnr = fnr.fnr_cli:main'
            ]
        })

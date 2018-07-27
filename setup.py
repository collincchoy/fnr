from setuptools import setup

setup(
        name = 'fnr',
        version = '0.1.1',
        packages = ['fnr'],
        test_suite = 'fnr.tests.fnrTests',
        setup_requires = ['nose>=1.0'],
        entry_points = {
            'console_scripts': [
                'fnr = fnr.fnr_cli:main'
            ]
        }
)

from setuptools import setup, find_packages

setup(
    name='tercen',
    version='0.1.11',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy==1.23.4',
        'pandas==1.5.1',
        'python-dateutil==2.8.2',
        'pytz==2022.6',
        'scipy==1.10.0',
        'pytson @ git+https://github.com/tercen/pytson@1.5#egg=pytson'
    ],


)

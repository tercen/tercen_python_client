from setuptools import setup, find_packages

setup(
    name='tercen',
    version='0.1.16',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy==1.23.5',
        'pandas==1.1.5',
        'python-dateutil==2.8.2',
        'pytz==2022.6',
        'scipy==1.10.0',
        'pytson @ git+https://github.com/tercen/pytson@1.6.1#egg=pytson'
    ],


)

from setuptools import setup, find_packages

setup(
    name='tercen',
    version='0.4.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy==1.23.*',
        'pandas==1.1.*',
        'python-dateutil==2.8.*',
        'pytz==2022.6',
        'scipy==1.10.*',
        'pytson @ git+https://github.com/tercen/pytson@1.7.6#egg=pytson'
    ],


)

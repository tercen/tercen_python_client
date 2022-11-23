from setuptools import setup, find_packages

setup(
    name='tercen',
    version='0.0.2',
    packages=(
        find_packages(exclude="tests**") 
    ),
    install_requires=[
        'pandas >= 1.5, <1.6',
        'pytson @ git+https://github.com/tercen/pytson@1.5#egg=pytson'
    ],


)

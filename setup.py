from setuptools import setup, find_packages

setup(
    name='tercen',
    version='0.0.2',
    packages=(
        find_packages(exclude="tests**") 
    ),
)

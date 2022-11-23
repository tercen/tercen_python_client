from setuptools import setup, find_packages

setup(
    name='tercen',
    version='0.0.1',
    packages=(
        find_packages() + 
        find_packages(where="./tercen") 
    ),
)

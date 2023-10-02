from setuptools import setup, find_packages

setup(
    name='tercen_python_client',
    version='0.7.17',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy==1.24.*',
        'pandas==1.5.*',
        'python-dateutil==2.8.*',
        'pytz==2022.6',
        'scipy==1.10.*',
        'pytson @ git+https://github.com/tercen/pytson@1.7.6#egg=pytson',
        'polars==0.18.*',
        'pipreqs==0.4.*'
    ],


)

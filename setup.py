from setuptools import setup, find_packages

setup(
    name='tercen_python_client',
    version='0.12.12',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'numpy==1.22.*',
        'pandas==2.1.*',
        'python-dateutil==2.8.*',
        'pytz==2023.*',
        'scipy==1.11.*',
        'pytson @ git+https://github.com/tercen/pytson@1.8.10#egg=pytson',
        'polars==0.20.*',
        'pipreqs==0.4.*'
    ],


)
